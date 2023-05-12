CREATE DATABASE Sales;

--Table 1: SalesPeople

--Snum is Primary key

--Sname is Unique constraint

--Snum Sname City Comm

--1001 Peel. London .12

--1002  Serres Sanjose .13

--1004 Motika London .11

--1007 Rifkin Barcelona .15

--1003 Axelrod Newyork .10

CREATE TABLE SalesPeople(
	Snum INTEGER PRIMARY KEY,
	Sname VARCHAR(50) UNIQUE,
	City VARCHAR(50),
	Comm INTEGER
);

INSERT INTO SalesPeople
VALUES(1001,'Peel','London',12);

INSERT INTO SalesPeople
VALUES(1002,'Serres','Sanjose',13);

INSERT INTO SalesPeople
VALUES(1004,'Motika','London',11);

INSERT INTO SalesPeople
VALUES(1007,'Rifkin','Barcelona',15);

INSERT INTO SalesPeople
VALUES(1003,'Axelrod','Newyork',10);

--Table 2: Customers

--Cnum is Primary Key

--City has not null constraint .

--Snum is foreign key constraint refers Snum column of SalesPeople table.

--Cnum Cname City Snum

--2001  Hoffman London 1001

--2002  Giovanni Rome 1003

--2003  Liu Sanjose 1002

--2004  Grass Berlin 1002

--2006 Clemens London 1001

--2008 Cisneros Sanjose 1007

--2007 Pereira Rome 1004

CREATE TABLE Customers(
	Cnum INTEGER PRIMARY KEY,
	Cname VARCHAR(255),
	City VARCHAR(255) NOT NULL,
	Snum INTEGER,
	FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum)
);

INSERT INTO Customers
VALUES(2001,'Hoffman','London',1001);
INSERT INTO Customers
VALUES(2002,'Giovanni','Rome',1003);
INSERT INTO Customers
VALUES(2003,'Liu','Sanjose',1002);
INSERT INTO Customers
VALUES(2004,'Grass','Berlin',1002);
INSERT INTO Customers
VALUES(2006,'Clemens','London',1001);
INSERT INTO Customers
VALUES(2008,'Cisneros','Sanjose',1007);
INSERT INTO Customers
VALUES(2007,'Pereira','Rome',1004);


--Table 3: Orders

--Onum is Primary key

--Cnum is foreign key refers to Cnum column of Customers table. Snum is foreign key refers Snum column of SalesPeople table.

--Onum Amt Odate Cnum Snum

--3001 18.69 3-10-1990 2008 1007

--3003 767.19 3-10-1990 2001 1001

--3002 1900.10 3-10-1990 2007 1004

--3005  5160.45 3-10-1990 2003 1002

--3006  1098.16 3-10-1990 2008 1007

--3009 1713.23 4-10-1990 2002 1003

--3007  75.75 4-10-1990 2004 1002

--3008  4273.00 5-10-1990 2006 1001

--3010  1309.95 6-10-1990 2004 1002

--3011  9891.88 6-10-1990 2006 1001

CREATE TABLE Orders(
	Onum INTEGER PRIMARY KEY,
	Amt INTEGER,
	Odate DATE,
	Cnum INTEGER,
	Snum INTEGER,
	FOREIGN KEY(Cnum) REFERENCES Customers(Cnum),
	FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum)
);

INSERT INTO Orders
VALUES(3001,18.69,'3-10-1990',2008,1007),
(3003,767.19,'3-10-1990',2001,1001),
(3002,1900.10,'3-10-1990',2007,1004),
(3005,5160.45,'3-10-1990',2003,1002),
(3006,1098.16,'3-10-1990',2008,1007),
(3009,1713.23,'4-10-1990',2002,1003),
(3007,75.75,'4-10-1990',2004,1002),
(3008,4273.00,'5-10-1990',2006,1001),
(3010,1309.95,'6-10-1990',2004,1002),
(3011,9891.88,'6-10-1990',2006,1001);

SELECT * 
FROM SalesPeople;

SELECT * 
FROM Customers; 

SELECT *
FROM Orders;

-- Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT COUNT(*) AS NameBeginWithaA
FROM SalesPeople
WHERE Sname LIKE '[aA]%';

-- Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT Snum,SUM(Amt) AS Total
FROM Orders
GROUP BY Snum
HAVING SUM(Amt) > 2000;

SELECT s.Sname,SUM(o.Amt) AS Total
FROM SalesPeople AS s
JOIN Orders AS o
ON s.Snum = o.Snum
GROUP BY s.Sname
HAVING SUM(Amt) > 2000;

-- Count the number of Salesperson belonging to Newyork.

SELECT COUNT(*) AS NewyorkRes
FROM SalesPeople
WHERE City = 'Newyork';

-- Display the number of Salespeople belonging to London and belonging to Paris.
SELECT COUNT(*) AS LonParRes
FROM SalesPeople
WHERE City IN ('London','Paris');

--Display the number of orders taken by each Salesperson and their date of orders.
SELECT Snum,Odate,COUNT(Onum) AS OrderCount
FROM Orders
GROUP BY Snum,Odate
ORDER BY Snum;

SELECT Odate,Snum,COUNT(Onum) AS OrderCount
FROM Orders
GROUP BY Odate,Snum
ORDER BY Odate;
