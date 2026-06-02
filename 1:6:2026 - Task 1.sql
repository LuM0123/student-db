CREATE DATABASE stu_db;
USE stu_db;

CREATE TABLE Students(
  StuID INT PRIMARY KEY,
  FirstName VARCHAR(30)NOT NULL,
  LastName VARCHAR (30)NOT NULL,
  Height VARCHAR (45)NOT NULL
);

INSERT INTO Students (StuID, FirstName, LastName, Height)
VALUES (01, 'Mary', 'Zhang', '167cm'),
       (02, 'Jason', 'Wang', '182cm'),
       (03, 'Alice', 'Chen', '164cm'),
       (04, 'Katy', 'Xu', '158cm');
       
SELECT * FROM Students;

DELETE FROM Students WHERE StuID = 03;

UPDATE Students
SET Height = '170cm'
WHERE StuID = 01;