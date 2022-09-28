SOURCE db_default.sql


SELECT * FROM Gender WHERE Name LIKE "%man";
/*
+----+-------+
| Id | Name  |
+----+-------+
|  1 | Man   |
|  2 | Woman |
+----+-------+
*/

SELECT * FROM Gender WHERE Name = "man";
/*
+----+------+
| Id | Name |
+----+------+
|  1 | Man  |
+----+------+
*/

SELECT * FROM User WHERE FirstName <> "jamshid";
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     |          | EYES     |        3 |
+----+-----------+----------+----------+----------+
*/

SELECT * FROM User WHERE id BETWEEN 3 AND 6;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  3 | Majid     |          | EYES     |        3 |
|  4 | Jamshid   |          | Jina001  |        3 |
|  5 | Jamshid   |          | Tk       |        3 |
|  6 | Jamshid   |          | JM       |        3 |
+----+-----------+----------+----------+----------+
*/

SELECT * FROM User WHERE id IN (1,2,3);
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     |          | EYES     |        3 |
+----+-----------+----------+----------+----------+
*/

SELECT * FROM User WHERE id = 3 OR id = 6;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  3 | Majid     |          | EYES     |        3 |
|  6 | Jamshid   |          | JM       |        3 |
+----+-----------+----------+----------+----------+
*/

SELECT * FROM User WHERE NOT id = 2 and NOT id = 3;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  4 | Jamshid   |          | Jina001  |        3 |
|  5 | Jamshid   |          | Tk       |        3 |
|  6 | Jamshid   |          | JM       |        3 |
+----+-----------+----------+----------+----------+
*/

SELECT Id FROM User WHERE UserName IS NOT NULL;
/*
+----+
| Id |
+----+
|  3 |
|  1 |
|  4 |
|  6 |
|  5 |
|  2 |
+----+
*/