-- FIT DATABASE UNDERGRADUATE UNITS ASSIGNMENT 2 / S1 / 2019
-- FILL IN THE FOLLOWING:
--Unit Code:FIT2094
--Student ID:29675952
--Student Full Name: Shlok Thakur
--Student email:stha0012@student.monash.edu
--Tutor Name: Harsha

/*  --- COMMENTS TO YOUR MARKER --------
RESERVE
    garage_code-
    vunit_id-
    reserve_date_time_placed-
    renter_no-

LOAN
    garage_code-
    vunit_id-
    loan_date_time- the date when the car is loaned
    loan_due_date- the date when the car is due
    loan_actual_return_date- the date when the car is actually returned
    renter_no- the id number of the rent
    
VEHICLE_UNIT
    garage_code
    vunit_id- the unique identifier of a specific vehicle
    vunit_purchase_price- the purchase price of the vehicle
    vunit_exhibition_flag- the exhibition flag
    vehicle_insurance_id- the insurance id of a vehicle
    vunit_rego- the rego for a specific car

MANAGEMENT_ASSIGN
    specialisation_type- this is what tha manager specialises in
    garage_code
    man_id
*/

--Q1
/*
TASK 1.1 BELOW
*/
---------- VEHICLE_UNIT ----------
CREATE TABLE vehicle_unit (
    garage_code NUMERIC(2) NOT NULL,
    vunit_id NUMERIC(6) NOT NULL,
    vunit_purchase_price NUMERIC(7,2) NOT NULL,
    vunit_exhibition_flag CHAR(1) NOT NULL,
    vehicle_insurance_id VARCHAR(20) NOT NULL,
    vunit_rego VARCHAR(8) NOT NULL
);

COMMENT ON COLUMN vehicle_unit.vunit_purchase_price IS
    'the purchase price of the vehicle';

COMMENT ON COLUMN vehicle_unit.vunit_exhibition_flag IS
    'the exhibition flag';

COMMENT ON COLUMN vehicle_unit.vehicle_insurance_id IS
    'the insurance id of a vehicle';

COMMENT ON COLUMN vehicle_unit.vunit_rego IS
    'the rego for a specific car';


ALTER TABLE vehicle_unit 
ADD CONSTRAINT vehicle_unit_pk 
PRIMARY KEY (garage_code,vunit_id);


ALTER TABLE vehicle_unit 
ADD CONSTRAINT vunit_rego_uq 
UNIQUE (vunit_rego);

---------- RESERVE ----------
CREATE TABLE reserve (
    garage_code NUMERIC(2) NOT NULL,
    vunit_id NUMERIC(6) NOT NULL,
    reserve_date_time_placed DATE NOT NULL,
    renter_no NUMERIC(6) NOT NULL
);
ALTER TABLE reserve 
ADD CONSTRAINT reserve_pk 
PRIMARY KEY (garage_code,vunit_id,reserve_date_time_placed);

---------- LOAN ----------
CREATE TABLE loan (
    garage_code NUMERIC(2) NOT NULL,
    vunit_id NUMERIC(6) NOT NULL,
    loan_date_time DATE NOT NULL,
    loan_due_date DATE,
    loan_actual_return_date DATE,
    renter_no NUMERIC(8) NOT NULL
);
ALTER TABLE loan 
ADD CONSTRAINT loan_pk 
PRIMARY KEY (garage_code,vunit_id,loan_date_time);

COMMENT ON COLUMN loan.loan_date_time IS
    'the date when the car is loaned';

COMMENT ON COLUMN loan.loan_due_date IS
    'the date when the car is due';

COMMENT ON COLUMN loan.loan_actual_return_date IS
    'the date when the car is actually returned';

---Alter FKs---
---------- VEHICLE_UNIT ----------
ALTER TABLE vehicle_unit
    ADD CONSTRAINT garage_vu FOREIGN KEY (garage_code)
        REFERENCES garage (garage_code);

ALTER TABLE vehicle_unit
    ADD CONSTRAINT vd_vu FOREIGN KEY (vehicle_insurance_id)
        REFERENCES vehicle_detail (vehicle_insurance_id);

---------- RESERVE ----------
ALTER TABLE reserve
    ADD CONSTRAINT vu_reserve 
    FOREIGN KEY (garage_code,vunit_id) REFERENCES vehicle_unit(garage_code,vunit_id);

ALTER TABLE reserve
    ADD CONSTRAINT renter_reserve 
    FOREIGN KEY (renter_no) REFERENCES renter(renter_no);
        
---------- LOAN ----------
ALTER TABLE loan
    ADD CONSTRAINT vu_loan 
    FOREIGN KEY (garage_code,vunit_id) REFERENCES vehicle_unit(garage_code,vunit_id);

ALTER TABLE loan
    ADD CONSTRAINT renter_loan 
    FOREIGN KEY (renter_no) REFERENCES renter(renter_no);

COMMIT;
/*
TASK 1.2 BELOW
*/
DROP TABLE vehicle_feature PURGE;
DROP TABLE feature PURGE;
DROP TABLE vendor_vehicle PURGE;
DROP TABLE reserve PURGE;
DROP TABLE loan PURGE;
DROP TABLE vendor PURGE; 
DROP TABLE renter PURGE;
DROP TABLE vehicle_unit PURGE;
DROP TABLE vehicle_detail PURGE;
DROP TABLE manufacturer PURGE;
DROP TABLE management_assign PURGE;
DROP TABLE garage PURGE;
DROP TABLE manager PURGE;
--Q2
/*
TASK 2.1 BELOW
*/
INSERT INTO vehicle_detail VALUES (
    'sports-ute-449-12b',
    'Toyota Hilux SR Manual 4x2 MY14',
    'M',
    200.00,
    TO_DATE('2018','YYYY'),
    4.0,
    (SELECT manufacturer_id FROM manufacturer WHERE manufacturer_name='Toyota')
);

INSERT INTO vehicle_feature Values(
    (SELECT feature_code FROM feature WHERE feature_details = 'metallic silver'),
    'sports-ute-449-12b'
);

INSERT INTO vehicle_feature VALUES (
    (SELECT feature_code FROM feature WHERE feature_details = 'aluminium tray'),
    'sports-ute-449-12b'
);

INSERT INTO vendor_vehicle VALUES (
    'sports-ute-449-12b',
    1
);

INSERT INTO vendor_vehicle VALUES (
    'sports-ute-449-12b',
    2
);

INSERT INTO vehicle_unit VALUES(
    (SELECT garage_code FROM garage WHERE garage_name='Caulfield VIC'),
    1,
    50000,
    'S',
    'sports-ute-449-12b',
    'RD3161'
);

INSERT INTO vehicle_unit VALUES(
    (SELECT garage_code FROM garage WHERE garage_name='South Yarra VIC'),
    2,
    50000,
    'S',
    'sports-ute-449-12b',
    'RD3141'
);

INSERT INTO vehicle_unit VALUES(
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    3,
    50000,
    'S',
    'sports-ute-449-12b',
    'RD3000'
);
COMMIT;
/*
TASK 2.2 BELOW
*/
CREATE SEQUENCE renter_no START WITH 10 NOCACHE ORDER;

/*
TASK 2.3 BELOW
*/
DROP SEQUENCE renter_no;


--Q3
/*
TASK 3.1 BELOW
*/
INSERT INTO renter VALUES (
    renter_no.nextval,
    'Van',
    'Diesel',
    'Oakpark Drive',
    'Chadstone',
    '3148',
    'vandiesel@gmail.com',
    0425715123,
    (SELECT garage_code FROM garage WHERE garage_name='Caulfield VIC')
);

COMMIT;
/*
TASK 3.2 BELOW
*/

INSERT INTO reserve VALUES (
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    (SELECT vunit_id FROM vehicle_unit WHERE vunit_rego = 'RD3000'),
    TO_DATE('04 04/04/2018','HH DD/MM/YYYY'),
    (SELECT renter_no FROM renter WHERE renter_fname='Van' and renter_lname = 'Diesel')
);

COMMIT;
/*

TASK 3.3 BELOW
*/
INSERT INTO loan VALUES (
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    (SELECT vunit_id FROM vehicle_unit WHERE vunit_rego = 'RD3000'),
    TO_DATE('02 11/04/2018','HH DD/MM/YYYY'),
    TO_DATE('02 11/04/2018','HH DD/MM/YYYY') + 7,
    NULL, --should this be null
    (SELECT renter_no FROM renter WHERE renter_fname='Van' and renter_lname = 'Diesel')
);
COMMIT;

/*
TASK 3.4 BELOW
*/
UPDATE loan
SET loan_actual_return_date = TO_DATE('02 18/04/2018','HH DD/MM/YYYY');

INSERT INTO loan VALUES (
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    (SELECT vunit_id FROM vehicle_unit WHERE vunit_rego = 'RD3000'),
    TO_DATE('02 18/04/2018','HH DD/MM/YYYY'),
    TO_DATE('02 18/04/2018','HH DD/MM/YYYY')+7,
    NULL,
    (SELECT renter_no FROM renter WHERE renter_fname='Van' and renter_lname = 'Diesel')
);
COMMIT;

--Q4
/*
TASK 4.1 BELOW
*/
ALTER TABLE vehicle_unit ADD damage_type CHAR(1);

UPDATE vehicle_unit SET damage_type = 'G';

ALTER TABLE vehicle_unit MODIFY damage_type NOT NULL;

ALTER TABLE vehicle_unit ADD CONSTRAINT vu_damage_type_chk CHECK (damage_type IN ('M','W','G'));

COMMIT;
/*
TASK 4.2 BELOW
*/
ALTER TABLE loan ADD return_garage_code NUMBER(2);
UPDATE loan SET return_garage_code = garage_code WHERE loan_actual_return_date IS NOT NULL;
COMMIT;

/*
TASK 4.3 BELOW
*/
CREATE TABLE management_assign (
    specialisation_type   VARCHAR(30) NOT NULL,
    garage_code      NUMBER(2) NOT NULL,
    man_id           NUMBER(2) NOT NULL
);

COMMENT ON COLUMN management_assign.specialisation_type IS
    'this is what the manager specialises in';


ALTER TABLE management_assign ADD CONSTRAINT specialisation_check CHECK (specialisation_type IN ('Full','Bikes','Motorcars','Sportscars'));

ALTER TABLE management_assign ADD CONSTRAINT management_assign_pk PRIMARY KEY (specialisation_type, garage_code );

ALTER TABLE management_assign ADD CONSTRAINT garage_management_assign FOREIGN KEY (garage_code) REFERENCES garage (garage_code);

ALTER TABLE management_assign ADD CONSTRAINT manager_management_assign FOREIGN KEY (man_id) REFERENCES manager (man_id);

--inserting Robert to Caufield
INSERT INTO management_assign VALUES (
    'Full',
    (SELECT garage_code FROM garage WHERE garage_name = 'Caulfield VIC'),
    1
);

--inserting Robert to Melbournce Central
INSERT INTO management_assign VALUES (
    'Sportscars',
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    1
);

--inserting Cat to Melbournce Central
INSERT INTO management_assign VALUES (
    'Bikes',
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    2
);
INSERT INTO management_assign VALUES (
    'Motorcars',
    (SELECT garage_code FROM garage WHERE garage_email='melbournec@rdbms.example.com'),
    2
);

--inserting Cat to South Yarra
INSERT INTO management_assign VALUES (
    'Full',
    (SELECT garage_code FROM garage WHERE garage_name='South Yarra VIC'),
    2
);
COMMIT;

