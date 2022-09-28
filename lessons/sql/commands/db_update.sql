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


UPDATE  User
SET     LastName = "Empty";
SELECT  * 
FROM    User;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     | Empty    | HamidA   |        3 |
|  2 | Saeed     | Empty    | TTop     |        3 |
|  3 | Majid     | Empty    | EYES     |        3 |
|  4 | Jamshid   | Empty    | Jina001  |        3 |
|  5 | Jamshid   | Empty    | Tk       |        3 |
|  6 | Jamshid   | Empty    | JM       |        3 |
+----+-----------+----------+----------+----------+
*/


UPDATE  User
SET     LastName = ""
WHERE   UserName = "TTop";
SELECT  * 
FROM    User;
/*
+----+-----------+----------+----------+----------+
| Id | FirstName | LastName | UserName | GenderId |
+----+-----------+----------+----------+----------+
|  1 | Hamid     | Empty    | HamidA   |        3 |
|  2 | Saeed     |          | TTop     |        3 |
|  3 | Majid     | Empty    | EYES     |        3 |
|  4 | Jamshid   | Empty    | Jina001  |        3 |
|  5 | Jamshid   | Empty    | Tk       |        3 |
|  6 | Jamshid   | Empty    | JM       |        3 |
+----+-----------+----------+----------+----------+
*/