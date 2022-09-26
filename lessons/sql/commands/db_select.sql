CREATE DATABASE IF NOT EXISTS MyDatabase;
USE MyDatabase;


DROP TABLE IF EXISTS Test;


CREATE TABLE IF NOT EXISTS Test(
    id  INTEGER
);


INSERT INTO Test (id) values(1);
INSERT INTO Test (id) values(2);
INSERT INTO Test (id) values(2);
INSERT INTO Test (id) values(2);
INSERT INTO Test (id) values(3);


SELECT * FROM Test;
SELECT DISTINCT * FROM Test;