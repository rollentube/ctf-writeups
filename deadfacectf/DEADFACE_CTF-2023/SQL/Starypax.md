# Starypax (50 points)
Starypax (street name STAR) is a controlled substance and is in high demand on the Dark Web. DEADFACE might leverage this database to find out which patients currently carry STAR.

How many patients in the Aurora database have an active prescription for Starypax as of Oct 20, 2023? And whose prescription expires first?

Submit the flag as `flag{#_firstname lastname}`.

Use the database dump from Aurora Compromise.

## Solution
The prescriptions are stored in the prescriptions table. In here is a row called drug_id. This table reference to the drugs table:
```
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
5 rows in set (0.000 sec)

MariaDB [ctf]> explain prescriptions;
+-----------------+---------------+------+-----+---------+----------------+
| Field           | Type          | Null | Key | Default | Extra          |
+-----------------+---------------+------+-----+---------+----------------+
| prescription_id | int(11)       | NO   | PRI | NULL    | auto_increment |
| patient_id      | int(11)       | NO   | MUL | NULL    |                |
| drug_id         | int(11)       | NO   | MUL | NULL    |                |
| doctor_id       | int(11)       | NO   | MUL | NULL    |                |
| date_prescribed | date          | NO   |     | NULL    |                |
| instructions    | varchar(4096) | YES  |     | NULL    |                |
| refills         | int(11)       | NO   |     | NULL    |                |
| expiration      | date          | NO   |     | NULL    |                |
+-----------------+---------------+------+-----+---------+----------------+
8 rows in set (0.001 sec)

MariaDB [ctf]> 
```

To get the amount we can use the following statement:
```
MariaDB [ctf]> select count(*) from prescriptions,drugs,patients where prescriptions.drug_id=drugs.drug_id and prescriptions.patient_id=patients.patient_id
and drugs.drug_name='Starypax' and prescriptions.expiration>current_date;
+----------+
| count(*) |
+----------+
|        7 |
+----------+
1 row in set (0.001 sec)

MariaDB [ctf]> 
```

To get the first expiry we have to join the table with the patients table as well:
```
MariaDB [ctf]> select patients.first_name,patients.last_name,prescriptions.expiration from prescriptions,drugs,patients where prescriptions.drug_id=drugs.drug_id and prescriptions.patient_id=patients.patient_id and drugs.drug_name='Starypax' and prescriptions.expiration>current_date order by prescriptions.expiration;
+------------+-----------+------------+
| first_name | last_name | expiration |
+------------+-----------+------------+
| Renae      | Allum     | 2023-10-26 |
| Chrissie   | Hargraves | 2023-10-28 |
| Eolanda    | Maciaszek | 2023-10-31 |
| Rodi       | Godfery   | 2023-11-04 |
| Chic       | Abrashkov | 2023-11-20 |
| Appolonia  | Benda     | 2023-11-26 |
| Lenci      | Springett | 2023-12-19 |
+------------+-----------+------------+
7 rows in set (0.001 sec)

MariaDB [ctf]> 
```

So the flag is: `flag{7_Renae Allum}`