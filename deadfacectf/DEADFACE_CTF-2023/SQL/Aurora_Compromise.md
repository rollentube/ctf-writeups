# Aurora Compromise (10 points)
DEADFACE has taken responsibility for a partial database hack on a pharmacy tied to Aurora Pharmaceuticals. The hacked data consists of patient data, staff data, and information on drugs and prescriptions.

We’ve managed to get a hold of the hacked data. Provide the first and last name of the patient that lives on a street called Hansons Terrace.

Submit the flag as: `flag{First Last}`.

[Download Database Dump](https://tinyurl.com/ytsdav3b)
SHA1: 35717ca5c498d90458478ba9f72557c62042373f

[Download System Design Specification](https://tinyurl.com/3z7zf9y9)
SHA1: d6627aa2099a5707d34e26fc82bb532af6398575

## Solution
To read out the SQL file we could create a local SQL database and import the file. After that we can analyse the database with SQL statements.

But SQL files are also just plain text. So we can grep with regex for the right entry as well:
```
$ grep -o -E "(.{0,90}Hansons Terrace.{0,50})" aurora.sql
'PA','19191','1955-08-05'),(10562,'Sandor','Beyer','V','Male','sbeyer1uz@time.com','20263 Hansons Terrace','Sacramento','CA','94207','1980-05-03'),(10563,'
$
```

The flag is: `flag{Sandor Beyer}`

### Setting up database
Since I saw that all SQL challenges use this database backup, I set up a SQL server anyway:
```
$ sudo systemctl start mariadb.service
$ mysql -h 127.0.0.1 -P 3306 -u root -p 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 39
Server version: 10.11.4-MariaDB-1 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| empire             |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.055 sec)

MariaDB [(none)]> create database ctf;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| ctf                |
| empire             |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.000 sec)

MariaDB [(none)]> use ctf;
Database changed
MariaDB [ctf]> source aurora.sql;
Query OK, 0 rows affected (0.000 sec)

Query OK, 0 rows affected (0.000 sec)

Query OK, 0 rows affected (0.000 sec)

Query OK, 0 rows affected (0.000 sec)

[...]

MariaDB [ctf]> show tables;
+--------------------+
| Tables_in_ctf      |
+--------------------+
| billing            |
| credit_types       |
| drugs              |
| facilities         |
| insurors           |
| inventory          |
| orders             |
| patients           |
| positions          |
| positions_assigned |
| prescriptions      |
| staff              |
| suppliers          |
| transactions       |
+--------------------+
14 rows in set (0.000 sec)

MariaDB [ctf]> 
```

Now we can get the first SQL flag with a SQL statement:
```
MariaDB [ctf]> explain patients;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| patient_id | int(11)      | NO   | PRI | NULL    | auto_increment |
| first_name | varchar(32)  | NO   |     | NULL    |                |
| last_name  | varchar(64)  | NO   |     | NULL    |                |
| middle     | varchar(8)   | YES  |     | NULL    |                |
| sex        | varchar(8)   | NO   |     | NULL    |                |
| email      | varchar(128) | NO   | UNI | NULL    |                |
| street     | varchar(64)  | NO   |     | NULL    |                |
| city       | varchar(64)  | NO   |     | NULL    |                |
| state      | varchar(8)   | NO   |     | NULL    |                |
| zip        | varchar(12)  | NO   |     | NULL    |                |
| dob        | date         | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
11 rows in set (0.001 sec)

MariaDB [ctf]> select first_name,last_name from patients where street like '%Hansons Terrace';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Sandor     | Beyer     |
+------------+-----------+
1 row in set (0.008 sec)

MariaDB [ctf]> 
```