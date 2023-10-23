# City Hoard (100 points)
Aurora is asking for help in determining which city has the facility with the largest inventory of Remizide based on the Aurora database.

Submit the flag as `flag{city}`.

Use the database dump from Aurora Compromise.

## Solution
The relevant tables that we have to join are:
```
MariaDB [ctf]> explain inventory;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| inv_id      | int(11)     | NO   | PRI | NULL    | auto_increment |
| drug_id     | int(11)     | NO   | MUL | NULL    |                |
| facility_id | int(11)     | NO   | MUL | NULL    |                |
| locator     | varchar(24) | NO   |     | NULL    |                |
| qty         | int(11)     | NO   |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
5 rows in set (0.001 sec)

MariaDB [ctf]> explain facilities;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| facility_id | int(11)     | NO   | PRI | NULL    | auto_increment |
| phone       | varchar(12) | NO   | UNI | NULL    |                |
| street      | varchar(64) | NO   |     | NULL    |                |
| city        | varchar(64) | NO   |     | NULL    |                |
| state       | varchar(8)  | NO   |     | NULL    |                |
| zip         | varchar(12) | NO   |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
6 rows in set (0.000 sec)

MariaDB [ctf]> explain drugs;
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| drug_id     | int(11)       | NO   | PRI | NULL    | auto_increment |
| drug_name   | varchar(56)   | NO   | UNI | NULL    |                |
| description | varchar(4096) | NO   |     | NULL    |                |
| supplier_id | int(11)       | NO   | MUL | NULL    |                |
| cost        | float         | YES  |     | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
5 rows in set (0.001 sec)

MariaDB [ctf]> 
```

To get the city of the facility with the largest inventory of Remizide we can use:
```
MariaDB [ctf]> select inventory.qty,drugs.drug_name,facilities.city from inventory,drugs,facilities where inventory.drug_id=drugs.drug_id and drugs.drug_name='Remizide' and inventory.facility_id=facilities.facility_id order by inventory.qty;

[...]

| 2988 | Remizide  | West Palm Beach   |
| 2991 | Remizide  | Lansing           |
| 2992 | Remizide  | Seattle           |
| 2996 | Remizide  | Tulsa             |
| 2999 | Remizide  | Miami             |
+------+-----------+-------------------+
1209 rows in set (0.006 sec)

MariaDB [ctf]> 
```

The flag is `flag{Miami}`