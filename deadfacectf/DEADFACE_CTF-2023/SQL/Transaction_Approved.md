# Transaction Approved (100 points)
Turbo Tactical wants you to determine how many credit cards are still potentially at risk of being used by DEADFACE. How many credit cards in the Aurora database are NOT expired as of Oct 2023?

Submit the flag as `flag{#}`.

Use the database dump from Aurora Compromise.

## Solution
The credit card information is stored in the billing table:
```
MariaDB [ctf]> explain billing;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| billing_id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| patient_id     | int(11)     | NO   | MUL | NULL    |                |
| credit_type_id | int(11)     | NO   | MUL | NULL    |                |
| card_num       | varchar(24) | NO   | UNI | NULL    |                |
| exp            | varchar(8)  | NO   |     | NULL    |                |
| ccv            | varchar(4)  | NO   |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
6 rows in set (0.002 sec)

MariaDB [ctf]> 
```

To get the cards that are not expired as of October 2023 we can use:
```
MariaDB [ctf]> select count(*) from billing where exp>'2023-10';
+----------+
| count(*) |
+----------+
|     8785 |
+----------+
1 row in set (0.004 sec)

MariaDB [ctf]> 
```

So the flag is: `flag{8785}`