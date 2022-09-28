SOURCE db_default.sql


SELECT  min(id) 
FROM    User;
/*
+---------+
| min(id) |
+---------+
|       1 |
+---------+
*/


SELECT  avg(id) 
FROM    User;
/*
+---------+
| avg(id) |
+---------+
|  3.5000 |
+---------+
*/


SELECT  max(id) 
FROM    User;
/*
+---------+
| max(id) |
+---------+
|       6 |
+---------+
*/


SELECT  count(id) 
FROM    User;
/*
+-----------+
| count(id) |
+-----------+
|         6 |
+-----------+
*/


SELECT  sum(id) 
FROM    User;
/*
+---------+
| sum(id) |
+---------+
|      21 |
+---------+
*/


SELECT  UserName, length(UserName) as len
FROM    User;
/*
+----------+-----+
| UserName | len |
+----------+-----+
| EYES     |   4 |
| HamidA   |   6 |
| Jina001  |   7 |
| JM       |   2 |
| Tk       |   2 |
| TTop     |   4 |
+----------+-----+
*/


SELECT  trim(concat(" ", FirstName, "-", UserName)) as Name
FROM    User;
/*
+-----------------+
| Name            |
+-----------------+
| Hamid-HamidA    |
| Saeed-TTop      |
| Majid-EYES      |
| Jamshid-Jina001 |
| Jamshid-Tk      |
| Jamshid-JM      |
+-----------------+
*/


SELECT  upper(FirstName) as FN, lower(UserName) as un
FROM    User;
/*
+---------+---------+
| FN      | un      |
+---------+---------+
| HAMID   | hamida  |
| SAEED   | ttop    |
| MAJID   | eyes    |
| JAMSHID | jina001 |
| JAMSHID | tk      |
| JAMSHID | jm      |
+---------+---------+
*/


SELECT  avg, ceil(avg), round(avg), floor(avg), abs(avg), sign(avg)
FROM    (SELECT avg(id) as avg FROM User) as result;
/*
+--------+-----------+------------+------------+----------+-----------+
| avg    | ceil(avg) | round(avg) | floor(avg) | abs(avg) | sign(avg) |
+--------+-----------+------------+------------+----------+-----------+
| 3.5000 |         4 |          4 |          3 |   3.5000 |         1 |
+--------+-----------+------------+------------+----------+-----------+
*/


SELECT  id as ID, IF(mod(id,2) = 1, "Odd", "Even") as EvenOrOdd
FROM User;
/*
+----+-----------+
| ID | EvenOrOdd |
+----+-----------+
|  3 | Odd       |
|  1 | Odd       |
|  4 | Even      |
|  6 | Even      |
|  5 | Odd       |
|  2 | Even      |
+----+-----------+
*/

SELECT  least(min(id), avg(id), max(id)) as L, 
        greatest(min(id), avg(id), max(id)) as G
FROM User;
/*
+--------+--------+
| L      | G      |
+--------+--------+
| 1.0000 | 6.0000 |
+--------+--------+
*/