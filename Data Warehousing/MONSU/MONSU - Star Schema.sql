DROP TABLE category_dim CASCADE CONSTRAINTS PURGE;

CREATE TABLE category_dim AS
SELECT * FROM MClub.category;

DROP TABLE campus_dim CASCADE CONSTRAINTS PURGE;

CREATE TABLE campus_dim AS
SELECT DISTINCT Campus
FROM MClub.Event;

DROP TABLE courselevel_dim CASCADE CONSTRAINTS PURGE;

CREATE TABLE courselevel_dim AS
SELECT DISTINCT CourseLevel
FROM MClub.Student;

DROP TABLE semester_dim CASCADE CONSTRAINTS PURGE;

CREATE TABLE semester_dim (
semid VARCHAR2(10),
sem_desc VARCHAR2(20),
begin_date DATE,
end_date DATE
);

DROP TABLE eventsize_dim CASCADE CONSTRAINTS PURGE;

CREATE TABLE eventsize_dim (
event_size_type VARCHAR2(10),
sizedesc VARCHAR2(30)
);

INSERT INTO eventsize_dim
VALUES ('Small','<=10 Students');

INSERT INTO eventsize_dim
VALUES ('Medium','>21 and <= 80 Students');

INSERT INTO eventsize_dim
VALUES ('Large','>80 Students');

-- populate semester dimension for Semester 1 and Semester 2 and Summer and Winter Semester
-- (the begin and end date can be changed accoding to the case)
INSERT INTO semester_dim
VALUES ('S1', 'Semester1', TO_DATE('01-MAR', 'DD-MON'),
TO_DATE('30-JUN', 'DD-MON'));
INSERT INTO semester_dim
VALUES ('S2', 'Semester2', TO_DATE('01-AUG', 'DD-MON'),
TO_DATE('30-NOV', 'DD-MON'));
INSERT INTO semester_dim
VALUES ('WS', 'Winter Semester', TO_DATE('01-JUL', 'DD-MON'),
TO_DATE('31-JUL', 'DD-MON'));
INSERT INTO semester_dim
VALUES ('SS', 'Summer Semester', TO_DATE('01-DEC', 'DD-MON'),
TO_DATE('28-FEB', 'DD-MON'));

DROP TABLE temp_fact_monsu CASCADE CONSTRAINTS PURGE;

CREATE TABLE temp_fact_monsu AS
SELECT reg.RegistrationID,e.StartDate,e.MaxNumberInvolved, e.Campus,cat.Category,s.CourseLevel , e.EventFee 
FROM MClub.Event e, MClub.Registration reg , MClub.Category cat,MClub.Student s,MClub.Club c
WHERE reg.EventID = e.EventID
AND reg.StudentID = s.StudentID
AND e.ClubID = c.ClubID
AND c.CategoryID = cat.CategoryID
GROUP BY reg.RegistrationID, e.StartDate, e.MaxNumberInvolved,e.Campus,cat.Category,s.CourseLevel , e.EventFee; 

ALTER TABLE temp_fact_monsu
ADD (semid VARCHAR2(10));

ALTER TABLE temp_fact_monsu
ADD (event_size_type VARCHAR(10));

UPDATE temp_fact_monsu
SET semid = 'S1'
WHERE to_char(StartDate, 'MMDD') >= '0301'
AND to_char(StartDate, 'MMDD') <= '0630';

UPDATE temp_fact_monsu
SET semid = 'S2'
WHERE to_char(StartDate, 'MMDD') >= '0801'
AND to_char(StartDate, 'MMDD') <= '1130';

UPDATE temp_fact_monsu
SET semid = 'SW'
WHERE to_char(StartDate, 'MMDD') >= '0701'
AND to_char(StartDate, 'MMDD') <= '0730';

UPDATE temp_fact_monsu
SET semid = 'SS'
WHERE to_char(StartDate, 'MMDD') >= '1201'
AND to_char(StartDate, 'MMDD') <= '0228';

UPDATE temp_fact_monsu
SET event_size_type = 'Small'
WHERE MaxNumberInvolved <= 20;

UPDATE temp_fact_monsu
SET event_size_type = 'Medium'
WHERE MaxNumberInvolved > 20
AND MaxNumberInvolved <= 80;

UPDATE temp_fact_monsu
SET event_size_type = 'Large'
WHERE MaxNumberInvolved > 80;

DROP table fact_monsu CASCADE CONSTRAINTS PURGE;

CREATE table fact_monsu as
select T.campus,T.category,T.courselevel,T.semid,T.event_size_type,count(T.registrationid) as no_registered_students, sum(T.eventfee) as total_expenses
from temp_fact_monsu T
GROUP BY T.campus,T.category,T.courselevel,T.semid,T.event_size_type;

-- a)
SELECT semid, event_size_type, sum(no_registered_students) as no_registered_students
FROM fact_monsu
GROUP BY semid, event_size_type
ORDER BY semid;

-- b) 
SELECT campus, sum(total_expenses) as total_expenses
FROM fact_monsu
GROUP BY campus
ORDER BY total_expenses;

-- c)
SELECT category, sum(no_registered_students) as no_registered_students
FROM fact_monsu
GROUP BY category
ORDER BY category;

SELECT courselevel,sum(total_expenses) as total_expenses
FROM fact_monsu
WHERE category = 'Special Interest Club'
GROUP BY courselevel;

