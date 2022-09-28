SOURCE db_default.sql


SELECT  Id, UserName 
FROM    User
ORDER BY id ASC
LIMIT 3;
/*
+----+----------+
| Id | UserName |
+----+----------+
|  1 | HamidA   |
|  2 | TTop     |
|  3 | EYES     |
+----+----------+

*/

SELECT  *, count(FirstName) as count
FROM    User 
GROUP BY FirstName
ORDER BY id DESC;
/*
+----+-----------+----------+----------+----------+-------+
| Id | FirstName | LastName | UserName | GenderId | count |
+----+-----------+----------+----------+----------+-------+
|  4 | Jamshid   |          | Jina001  |        3 |     3 |
|  3 | Majid     |          | EYES     |        3 |     1 |
|  2 | Saeed     |          | TTop     |        3 |     1 |
|  1 | Hamid     |          | HamidA   |        3 |     1 |
+----+-----------+----------+----------+----------+-------+
*/

SELECT  id, UserName, count(*) as count 
FROM    User 
GROUP BY FirstName
ORDER BY id ASC, UserName DESC, count ASC;
/*
+----+----------+-------+
| id | UserName | count |
+----+----------+-------+
|  1 | HamidA   |     1 |
|  2 | TTop     |     1 |
|  3 | EYES     |     1 |
|  4 | Jina001  |     3 |
+----+----------+-------+
*/