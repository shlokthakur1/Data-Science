--SELECT sum(TotalPrice) FROM MRECOMANY.invoice WHERE TO_CHAR(invoicedate,'YYYY') = '2019';
--SELECT * FROM MRECOMANY.contract;

--Create Dimensions

DROP TABLE Utility_Dim CASCADE CONSTRAINTS PURGE;
CREATE TABLE Utility_Dim AS SELECT * FROM MRECOMANY.utilities;

DROP TABLE CompanySize_Dim CASCADE CONSTRAINTS PURGE;
CREATE TABLE CompanySize_Dim (
    SizeID VARCHAR(15),
    MinNoEmployees VARCHAR(15),
    MaxNoEmployees VARCHAR(15)
);

INSERT INTO CompanySize_Dim
 VALUES('Small',0,20);
INSERT INTO CompanySize_Dim
 VALUES('Medium',20,100);
INSERT INTO CompanySize_Dim
 VALUES('Large', 100,'Infinity' );

DROP TABLE Duration_Dim CASCADE CONSTRAINTS PURGE;
CREATE TABLE Duration_Dim (
    DurationID VARCHAR(15),
    MinNoYears VARCHAR(15),
    MaxNoYears VARCHAR(15)
);

INSERT INTO Duration_Dim
 VALUES('Short-term',0,1);
INSERT INTO Duration_Dim
 VALUES('Medium-term',1,5);
INSERT INTO Duration_Dim
 VALUES('Long-term', 5,'Infinity');

DROP TABLE Time_Dim CASCADE CONSTRAINTS PURGE;
CREATE TABLE Time_Dim AS SELECT DISTINCT
    to_char(inv.InvoiceDate,'QYYYY') as TimeID,
    to_char(inv.InvoiceDate,'q') as QuarterID,
    to_char(inv.InvoiceDate,'YYYY') as YearID
FROM MREComany.invoice inv;

-- Create Contract Fact
DROP TABLE TempContractFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE TempContractFact AS
SELECT c.clientid,c.contractid, c.ContractSignedDate, c.LeasingStartDate, c.LeasingEndDate, cl.NumberOfEmployees
FROM MREComany.contract c, MREComany.client cl
WHERE c.clientid = cl.clientid
GROUP BY c.clientid,c.contractid,c.ContractSignedDate, c.LeasingStartDate, c.LeasingEndDate, cl.NumberOfEmployees;

ALTER TABLE TempContractFact
ADD (SizeID VARCHAR2(15));

UPDATE TempContractFact
SET SizeID = 'Small'
WHERE NumberOfEmployees <= 20;

UPDATE TempContractFact
SET SizeID = 'Medium'
WHERE NumberOfEmployees > 20
AND NumberOfEmployees <= 100;

UPDATE TempContractFact
SET SizeID = 'Large'
WHERE NumberOfEmployees > 100;

ALTER TABLE TempContractFact
ADD (TimeID VARCHAR2(15));

UPDATE TempContractFact
SET TimeID = to_char(ContractSignedDate,'QYYYY');

ALTER TABLE TempContractFact
ADD (DurationLength VARCHAR(40));

UPDATE TempContractFact
SET DurationLength = months_between(leasingenddate,leasingstartdate);

ALTER TABLE TempContractFact
ADD (DurationID VARCHAR(15));

UPDATE TempContractFact
SET DurationID = 'Short-Term'
WHERE DurationLength < 12;

UPDATE TempContractFact
SET DurationID = 'Medium-Term'
WHERE DurationLength >= 12
AND DurationLength <= 60;

UPDATE TempContractFact
SET DurationID = 'Long-Term'
WHERE DurationLength > 60;

DROP TABLE ContractFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE ContractFact AS
SELECT SizeID, DurationID, TimeID, count(contractid) as NumOfContracts
FROM TempContractFact
GROUP BY SizeID, DurationID, TimeID;

--Create Invoice Fact
DROP TABLE TempInvoiceFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE TempInvoiceFact AS
SELECT inv.totalprice,inv.invoicedate,cl.numberofemployees
FROM MREComany.invoice inv, MREComany.client cl
WHERE inv.clientid = cl.clientid
GROUP BY inv.invoiceid,cl.clientid, inv.totalprice,inv.invoicedate,cl.numberofemployees;

ALTER TABLE TempInvoiceFact
ADD (SizeID VARCHAR2(15));

UPDATE TempInvoiceFact
SET SizeID = 'Small'
WHERE NumberOfEmployees <= 20;

UPDATE TempInvoiceFact
SET SizeID = 'Medium'
WHERE NumberOfEmployees > 20
AND NumberOfEmployees <= 100;

UPDATE TempInvoiceFact
SET SizeID = 'Large'
WHERE NumberOfEmployees > 100;

ALTER TABLE TempInvoiceFact
ADD (TimeID VARCHAR2(15));

UPDATE TempInvoiceFact
SET TimeID = to_char(invoicedate,'QYYYY');

DROP TABLE InvoiceFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE InvoiceFact AS
SELECT SizeID, TimeID, sum(TotalPrice) as TotalLeasingRevenue
FROM TempInvoiceFact
GROUP BY SizeID, TimeID;

-- Create Utility Fact
DROP TABLE TempUtilityFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE TempUtilityFact AS
SELECT u.utilitiesid,u.description, uu.consumptionenddate, uu.totalprice
FROM MREComany.utilities u, MREComany.utilities_used uu
WHERE u.utilitiesid = uu.utilitiesid
GROUP BY u.utilitiesid,u.description, uu.consumptionenddate, uu.totalprice;

ALTER TABLE TempUtilityFact
ADD (TimeID VARCHAR2(15));

UPDATE TempUtilityFact
SET TimeID = to_char(consumptionenddate,'QYYYY');

DROP TABLE UtilityFact CASCADE CONSTRAINTS PURGE;
CREATE TABLE UtilityFact AS
SELECT UtilitiesID,TimeID, sum(TotalPrice) as TotalServiceCharged
FROM TempUtilityFact
GROUP BY UtilitiesID, TimeID;

-- Querries
-- 1
SELECT SizeID, sum(TotalLeasingRevenue) as TotalLeasingRevenue
FROM InvoiceFact
WHERE substr(TimeID,2,5) = '2019'
GROUP BY SizeID;

-- 2
SELECT TimeID,UtilitiesID,sum(TotalServiceCharged) as TotalServiceCharged
FROM UtilityFact
WHERE UtilitiesID = 'U001'
AND TimeID = '12016'
GROUP BY UtilitiesID,TimeID;

-- 3
SELECT DurationID,sum(NumOfContracts) as NumOfContracts
FROM ContractFact
WHERE SizeID = 'Large'
GROUP BY DurationID;

-- 4
SELECT SizeID, substr(TimeID,2,5) as Year ,sum(NumOfContracts) as NumOfContracts
FROM ContractFact
GROUP BY SizeID,substr(TimeID,2,5)
ORDER BY NumOfContracts DESC;

