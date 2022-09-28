-------------------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS TestDataBase;
USE TestDataBase;

-------------------------------------------------------------------------------
DROP TABLE IF EXISTS Gender;
CREATE TABLE Gender(
    Id        INTEGER       NOT NULL    AUTO_INCREMENT,
    Name      VARCHAR(10)   NOT NULL                  ,

    PRIMARY KEY (Id)
);


INSERT INTO Gender (Name) VALUES ("Man");
INSERT INTO Gender (Name) VALUES ("Woman");
INSERT INTO Gender (Name) VALUES ("Unset");


SELECT * FROM Gender;

-------------------------------------------------------------------------------
DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User(
    Id          INTEGER     NOT NULL    AUTO_INCREMENT,
    FirstName   VARCHAR(99) NOT NULL    DEFAULT     "",
    LastName    VARCHAR(99) NOT NULL    DEFAULT     "",
    UserName    VARCHAR(30) NOT NULL    UNIQUE,
    GenderId    INTEGER     NOT NULL    DEFAULT     3,

    PRIMARY KEY(id)
);


INSERT INTO User (FirstName,UserName) values ("Hamid",  "HamidA"  );
INSERT INTO User (FirstName,UserName) values ("Saeed",  "TTop"    );
INSERT INTO User (FirstName,UserName) values ("Majid",  "EYES"    );
INSERT INTO User (FirstName,UserName) values ("Jamshid","Jina001" );
INSERT INTO User (FirstName,UserName) values ("Jamshid","Tk"      );
INSERT INTO User (FirstName,UserName) values ("Jamshid","JM"      );


SELECT * FROM User;