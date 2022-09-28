SOURCE db_default.sql

SELECT  *
FROM    User;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     |          | EYES     |        3 |
|  4 | Jamshid   |          | Jina001  |        3 |
|  5 | Jamshid   |          | Tk       |        3 |
|  6 | Jamshid   |          | JM       |        3 |
+----+-----------+----------+----------+----------+
*/

DELETE 
FROM    User
WHERE   FirstName = "jamshid";
SELECT  *
FROM    User;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     |          | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     |          | EYES     |        3 |
+----+-----------+----------+----------+----------+
*/