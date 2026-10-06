-- 1. CREATE DATABASE
CREATE DATABASE banking_db;
USE banking_db;


-- 2. CREATE ACCOUNTS TABLE
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    account_type VARCHAR(30),
    balance DECIMAL(10,2),
    city VARCHAR(50)
);



-- 3. INSERT SAMPLE DATA
INSERT INTO accounts VALUES
(101, 'Arun Kumar', 'Savings', 45000, 'Hyderabad'),
(102, 'Meera Shah', 'Current', 85000, 'Mumbai'),
(103, 'Ravi Reddy', 'Savings', 32000, 'Hyderabad'),
(104, 'Priya Nair', 'Savings', 67000, 'Bangalore'),
(105, 'Sameer Khan', 'Current', 120000, 'Pune'),
(106, 'Neha Gupta', 'Savings', 28000, 'Delhi'),
(107, 'Vikram Rao', 'Current', 95000, 'Hyderabad'),
(108, 'Anjali Singh', 'Savings', 54000, 'Mumbai');



-- 4. VIEW ACCOUNT DATA
SELECT * FROM accounts;



-- 5. GET ALL ACCOUNTS
DELIMITER //

CREATE PROCEDURE GetAllAccounts()
BEGIN
    SELECT *
    FROM accounts;
END //

DELIMITER ;

CALL GetAllAccounts();



-- 6. GET SAVINGS ACCOUNTS
DELIMITER //

CREATE PROCEDURE GetSavingsAccounts()
BEGIN
    SELECT *
    FROM accounts
    WHERE account_type = 'Savings';
END //

DELIMITER ;

CALL GetSavingsAccounts();



-- 7. GET ACCOUNTS BY CITY
DELIMITER //

CREATE PROCEDURE GetAccountsByCity(
    IN p_city VARCHAR(50)
)
BEGIN
    SELECT *
    FROM accounts
    WHERE city = p_city;
END //

DELIMITER ;

CALL GetAccountsByCity('Hyderabad');



-- 8. GET ACCOUNTS ABOVE BALANCE
DELIMITER //

CREATE PROCEDURE GetAccountsAboveBalance(
    IN p_balance DECIMAL(10,2)
)
BEGIN
    SELECT *
    FROM accounts
    WHERE balance > p_balance;
END //

DELIMITER ;

CALL GetAccountsAboveBalance(50000);


-- 9. UPDATE ACCOUNT BALANCE
DELIMITER //

CREATE PROCEDURE UpdateAccountBalance(
    IN p_account_id INT,
    IN p_new_balance DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = p_new_balance
    WHERE account_id = p_account_id;
END //

DELIMITER ;

CALL UpdateAccountBalance(101, 50000);



-- 10. DEPOSIT AMOUNT
DELIMITER //

CREATE PROCEDURE DepositAmount(
    IN p_account_id INT,
    IN p_deposit DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance + p_deposit
    WHERE account_id = p_account_id;
END //

DELIMITER ;

CALL DepositAmount(102, 10000);



-- 11. WITHDRAW AMOUNT
DELIMITER //

CREATE PROCEDURE WithdrawAmount(
    IN p_account_id INT,
    IN p_withdraw DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance - p_withdraw
    WHERE account_id = p_account_id;
END //

DELIMITER ;

CALL WithdrawAmount(103, 5000);



-- 12. DELETE ACCOUNT
DELIMITER //

CREATE PROCEDURE DeleteAccount(
    IN p_account_id INT
)
BEGIN
    DELETE FROM accounts
    WHERE account_id = p_account_id;
END //

DELIMITER ;

CALL DeleteAccount(108);



-- 13. VIEW FINAL ACCOUNT DATA
SELECT * FROM accounts;
