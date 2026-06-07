CREATE DATABASE BankDB;

USE BankDB;


CREATE TABLE Loan_Accounts (
    AccNo INT PRIMARY KEY,
    Cust_Name VARCHAR(50),
    Loan_Amount DECIMAL(10,2),
    Instalments INT,
    Int_Rate DECIMAL(5,2),
    Start_Date DATE,
    Interest DECIMAL(12,2)
);

INSERT INTO Loan_Accounts
(AccNo, Cust_Name, Loan_Amount, Instalments, Int_Rate, Start_Date, Interest)
VALUES
(1, 'R.K. Gupta', 300000, 36, 12.00, '2009-07-19', NULL),
(2, 'S.P. Sharma', 500000, 48, 10.00, '2008-03-22', NULL),
(3, 'K.P. Jain', 300000, 36, NULL, '2007-03-08', NULL),
(4, 'M.P. Yadav', 800000, 60, 10.00, '2008-12-06', NULL),
(5, 'S.P. Sinha', 200000, 36, 12.50, '2010-01-03', NULL),
(6, 'P. Sharma', 700000, 60, 12.50, '2008-06-05', NULL),
(7, 'K.S. Dhall', 500000, 48, NULL, '2008-03-05', NULL);


-- Display the details of all the loans with less than 40 instalments.
SELECT *
FROM Loan_Accounts
WHERE Instalments < 40;

-- Display the AccNo and Loan_Amount of all the loans started before 01-04-2009.
SELECT AccNo, Loan_Amount
FROM Loan_Acc
WHERE Start_Date < '2009-04-01';

-- Display the Int_Rate of all the loans started after 01-04-2009.
SELECT Int_Rate
FROM Loan_Acc
WHERE Start_Date > '2009-04-01';


-- Display the details of all the loans whose rate of interest is NULL.
SELECT *
FROM Loan_Acc
WHERE Int_Rate IS NULL;


-- Display the details of all the loans whose rate of interest is not NULL.
SELECT *
FROM Loan_Acc
WHERE Int_Rate IS NOT NULL;