# Counting STARs (150 points)
We know DEADFACE is trying to get their hands on STAR, so it makes sense that they will try to target the doctor who prescribes the most STAR from the Aurora database. Provide the first and last name and the type of doctor (position name) that prescribed the most STAR from the database.

Submit the flag as `flag{FirstName LastName Position}`.

For example: `flag{John Doe Podiatrist}`

Use the database dump from Aurora Compromise.

## Solution
For that challenge we have to join several tables. The relevant are prescriptions, drugs, positions_assigned, positions and staff.

To join them we use the id's, look for the drug Starypax and group the results for the doctor:
```
MariaDB [ctf]> select count(*) as amount,prescriptions.doctor_id,staff.first_name,staff.last_name,positions.position_name from prescriptions,drugs,positions_assigned,positions,staff where drugs.drug_id=prescriptions.drug_id and drugs.drug_name='Starypax' and prescriptions.doctor_id=positions_assigned.staff_id and positions.position_id=positions_assigned.position_id and staff.staff_id=positions_assigned.staff_id group by prescriptions.doctor_id order by amount;

[...]

|      5 |      2067 | Isadore    | Kubacek     | Family Medicine Physician |
|      6 |      1811 | Cristiano  | O`Hegertie  | Radiologist               |
|      6 |      1708 | Maude      | Cruden      | Pulmonologist             |
|      6 |      2003 | Keefer     | Schach      | Family Medicine Physician |
|      8 |      1957 | Alisa      | MacUchadair | Dermatologist             |
+--------+-----------+------------+-------------+---------------------------+
108 rows in set (0.011 sec)

MariaDB [ctf]> 
```
The flag is: `flag{Alisa MacUchadair Dermatologist}`