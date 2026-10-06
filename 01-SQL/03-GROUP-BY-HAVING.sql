USE training_db;

-- 1. COUNT - TOTAL EMPLOYEES
SELECT COUNT(*) AS total_employees
FROM employees;

-- 2. COUNT - EMPLOYEES IN EACH DEPARTMENT
SELECT department,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- 3. SUM - TOTAL SALARY
SELECT SUM(salary) AS total_salary
FROM employees;

-- 4. TOTAL SALARY BY DEPARTMENT
SELECT department,
SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 5. AVERAGE SALARY
SELECT AVG(salary) AS average_salary
FROM employees;

-- 6. AVERAGE SALARY BY DEPARTMENT
SELECT department,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- 7. MINIMUM SALARY BY DEPARTMENT
SELECT department,
       MIN(salary) AS minimum_salary
FROM employees
GROUP BY department;

-- 8. MAXIMUM SALARY BY DEPARTMENT
SELECT department,
       MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;

-- 9. GROUP BY WITH MULTIPLE AGGREGATE FUNCTIONS
SELECT department,
       COUNT(*) AS employee_count,
       SUM(salary) AS total_salary,
       AVG(salary) AS average_salary,
       MIN(salary) AS minimum_salary,
       MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;

-- 10. HAVING - DEPARTMENTS WITH MORE THAN 2 EMPLOYEES
SELECT department,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- 11. HAVING - DEPARTMENTS WITH TOTAL SALARY GREATER THAN 150000
SELECT department,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 150000;


-- 12. HAVING - DEPARTMENTS WITH AVERAGE SALARY GREATER THAN 60000
SELECT department,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
