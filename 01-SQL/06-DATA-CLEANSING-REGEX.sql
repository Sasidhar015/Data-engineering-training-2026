CREATE DATABASE registration_lab;
USE registration_lab;


-- 1. CREATE TABLE
CREATE TABLE registrations (
    registration_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    mobile VARCHAR(40),
    city VARCHAR(50),
    postal_code VARCHAR(20)
);


-- 2. INSERT RAW / DIRTY DATA
INSERT INTO registrations VALUES
(1, ' rohit sharma ', ' ROHIT@GMAIL.COM ', '+91-98765-43210', 'hyderabad', '500001'),
(2, 'SARA KHAN', 'sara@yahoo.com', '99887 66554', ' MUMBAI ', '400001'),
(3, ' amit patel ', '', '(040)99887766', 'Hyderabad', '500 032'),
(4, 'Neha Singh ', NULL, '9876543210', 'BANGALORE', '560001'),
(5, 'imran ali', 'IMRAN@MAIL.COM ', '91 9988772211', NULL, '500084'),
(6, 'Priya Rao', 'priya@gmail', '98765-AB210', 'Pune', '411001');



-- Q1. Remove spaces before/after names
SELECT
    full_name,
    TRIM(full_name) AS cleaned_name
FROM registrations;


-- Q2. Convert names to UPPERCASE
SELECT
    full_name,
    UPPER(TRIM(full_name)) AS cleaned_name
FROM registrations;



-- Q3. Convert emails to lowercase
SELECT
    email,
    LOWER(TRIM(email)) AS cleaned_email
FROM registrations;


-- Q4. Convert blank email values into NULL
SELECT
    email,
    NULLIF(TRIM(email), '') AS cleaned_email
FROM registrations;


-- Q5. Remove spaces and hyphens from mobiles
SELECT
    mobile,
    REPLACE(REPLACE(mobile, ' ', ''), '-', '') AS cleaned_mobile
FROM registrations;



-- Q6. Remove every non-numeric character
SELECT
    mobile,
    REGEXP_REPLACE(mobile, '[^0-9]', '') AS cleaned_mobile
FROM registrations;



-- Q7. Standardize city to UPPERCASE
SELECT
    city,
    UPPER(TRIM(city)) AS cleaned_city
FROM registrations;



-- Q8. Find records where city is NULL
SELECT *
FROM registrations
WHERE city IS NULL;



-- Q9. Find email values that are NULL or blank
SELECT *
FROM registrations
WHERE email IS NULL
   OR TRIM(email) = '';


-- Q10. Find only Gmail email addresses
SELECT
    email
FROM registrations
WHERE LOWER(TRIM(email))
      REGEXP '^[A-Za-z0-9._%+-]+@gmail\\.com$';



-- Q11. Identify incorrectly formatted emails
SELECT
    email,
    CASE
        WHEN email IS NULL OR TRIM(email) = ''
            THEN 'Missing'

        WHEN LOWER(TRIM(email))
             REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
            THEN 'Valid'

        ELSE 'Invalid'
    END AS email_status
FROM registrations;


-- Q12. Extract only numeric characters from postal codes
SELECT
    postal_code,
    REGEXP_REPLACE(postal_code, '[^0-9]', '') AS cleaned_postal_code
FROM registrations;


-- Q13. Find mobile numbers containing alphabets
SELECT
    registration_id,
    mobile
FROM registrations
WHERE mobile REGEXP '[A-Za-z]';



-- Q14. Produce completely cleaned output
SELECT
    registration_id,

    UPPER(TRIM(full_name)) AS cleaned_name,

    LOWER(NULLIF(TRIM(email), '')) AS cleaned_email,

    REGEXP_REPLACE(mobile, '[^0-9]', '') AS cleaned_mobile,

    UPPER(TRIM(city)) AS cleaned_city,

    REGEXP_REPLACE(postal_code, '[^0-9]', '') AS cleaned_postal_code

FROM registrations;



-- Q15. Create a cleaned copy in another table
CREATE TABLE registrations_cleaned AS
SELECT
    registration_id,

    UPPER(TRIM(full_name)) AS full_name,

    LOWER(NULLIF(TRIM(email), '')) AS email,

    REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile,

    UPPER(TRIM(city)) AS city,

    REGEXP_REPLACE(postal_code, '[^0-9]', '') AS postal_code

FROM registrations;


-- CHECK CLEANED TABLE
SELECT *
FROM registrations_cleaned;
