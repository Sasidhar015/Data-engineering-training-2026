-- Data Engineering Training 2026
-- SQL Basics Practice

-- 1. Select all records
SELECT *
FROM employees;

-- 2. Select specific columns
SELECT employee_id, employee_name, department
FROM employees;

-- 3. WHERE condition
SELECT *
FROM employees
WHERE department = 'IT';

-- 4. Comparison operators
SELECT *
FROM employees
WHERE salary > 50000;

-- 5. AND condition
SELECT *
FROM employees
WHERE department = 'IT'
  AND salary > 50000;

-- 6. OR condition
SELECT *
FROM employees
WHERE department = 'IT'
   OR department = 'HR';

-- 7. IN
SELECT *
FROM employees
WHERE department IN ('IT', 'HR');

-- 8. BETWEEN
SELECT *
FROM employees
WHERE salary BETWEEN 40000 AND 70000;

-- 9. LIKE
SELECT *
FROM employees
WHERE employee_name LIKE 'A%';

-- 10. IS NULL
SELECT *
FROM employees
WHERE city IS NULL;

-- 11. DISTINCT
SELECT DISTINCT department
FROM employees;

-- 12. Alias
SELECT employee_name AS name,
       salary AS monthly_salary
FROM employees;

-- 13. ORDER BY ascending
SELECT *
FROM employees
ORDER BY salary ASC;

-- 14. ORDER BY descending
SELECT *
FROM employees
ORDER BY salary DESC;
