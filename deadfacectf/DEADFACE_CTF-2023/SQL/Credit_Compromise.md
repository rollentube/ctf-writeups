# Credit Compromise (15 points)
How many credit cards were exposed in the Aurora database hack?

Submit the flag as `flag{#}`.

Use the database dump from Aurora Compromise.

## Solution
The credit cards numbers are stored in the billing table:
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
6 rows in set (0.001 sec)

MariaDB [ctf]> select count(*) from billing;
+----------+
| count(*) |
+----------+
|    10391 |
+----------+
1 row in set (0.003 sec)

MariaDB [ctf]> 
```

So the flag is `flag{10391}`