SOURCE db_default.sql


SELECT FirstName FROM User;
/*
+-----------+
| FirstName |
+-----------+
| Hamid     |
| Saeed     |
| Majid     |
| Jamshid   |
| Jamshid   |
| Jamshid   |
+-----------+
*/

SELECT DISTINCT Id,UserName FROM User;
/*
+----+----------+
| Id | UserName |
+----+----------+
|  3 | EYES     |
|  1 | HamidA   |
|  4 | Jina001  |
|  6 | JM       |
|  5 | Tk       |
|  2 | TTop     |
+----+----------+
*/

SELECT COUNT(DISTINCT id) FROM User;
/*
+--------------------+
| COUNT(DISTINCT id) |
+--------------------+
|                  6 |
+--------------------+
*/

SELECT * FROM User LIMIT 3;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     |          | EYES     |        3 |
+----+-----------+----------+----------+----------+
*/