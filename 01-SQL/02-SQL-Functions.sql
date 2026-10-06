USE training_db;

-- 1. STRING FUNCTIONS

-- UPPER()
SELECT UPPER(employee_name) AS upper_name
FROM employees;

-- LOWER()
SELECT LOWER(employee_name) AS lower_name
FROM employees;

-- LEN()
SELECT employee_name, LEN(employee_name) AS name_length
FROM employees;

-- CONCAT()
SELECT CONCAT(employee_name, ' - ', department) AS employee_details
FROM employees;


-- 2. MATHEMATICAL FUNCTIONS

-- ROUND()
SELECT employee_name, ROUND(salary, 0) AS rounded_salary
FROM employees;

-- CEILING()
SELECT employee_name, CEILING(salary / 1000.0) AS salary_ceiling
FROM employees;

-- FLOOR()
SELECT employee_name, FLOOR(salary / 1000.0) AS salary_floor
FROM employees;

-- ABS()
SELECT ABS(-500) AS absolute_value;

-- POWER()
SELECT POWER(2, 3) AS power_result;

-- SQRT()
SELECT SQRT(64) AS square_root;


-- 3. DATE FUNCTIONS

-- Current date and time
SELECT GETDATE() AS current_date_time;

-- YEAR()
SELECT YEAR(GETDATE()) AS current_year;

-- MONTH()
SELECT MONTH(GETDATE()) AS current_month;

-- DAY()
SELECT DAY(GETDATE()) AS current_day;

-- DATEADD()
SELECT DATEADD(DAY, 7, GETDATE()) AS date_after_7_days;

-- DATEDIFF()
SELECT DATEDIFF(DAY, '2026-01-01', GETDATE()) AS days_difference;


-- 4. AGGREGATE FUNCTIONS

-- COUNT()
SELECT COUNT(*) AS total_employees
FROM employees;

-- SUM()
SELECT SUM(salary) AS total_salary
FROM employees;

-- AVG()
SELECT AVG(salary) AS average_salary
FROM employees;

-- MIN()
SELECT MIN(salary) AS minimum_salary
FROM employees;

-- MAX()
SELECT MAX(salary) AS maximum_salary
FROM employees;
