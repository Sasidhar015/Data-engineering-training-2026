
CREATE DATABASE expense_db CHARACTER SET utf8mb4;
USE expense_db;

CREATE TABLE users (
    user_id         INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(100)  NOT NULL,
    email           VARCHAR(150)  NOT NULL UNIQUE,
    monthly_income  DECIMAL(12,2) NOT NULL DEFAULT 0,
    monthly_budget  DECIMAL(12,2) NOT NULL DEFAULT 0,
    created_at      TIMESTAMP     DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50) NOT NULL UNIQUE);

CREATE TABLE expenses (
    expense_id     INT AUTO_INCREMENT PRIMARY KEY,
    user_id        INT           NOT NULL,
    category_id    INT           NOT NULL,
    amount         DECIMAL(12,2) NOT NULL CHECK (amount > 0),
    expense_date   DATE          NOT NULL,
    description    VARCHAR(255),
    payment_method ENUM('Cash','Credit Card','Debit Card','UPI') DEFAULT 'Cash',
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_exp_user FOREIGN KEY (user_id)     REFERENCES users(user_id)           ON DELETE CASCADE,
    CONSTRAINT fk_exp_cat  FOREIGN KEY (category_id) REFERENCES categories(category_id),
    INDEX idx_user_date (user_id, expense_date),
    INDEX idx_category  (category_id));

INSERT INTO categories (name) VALUES
 ('Groceries'),('Rent'),('Utilities'),('Transport'),('Dining'),
 ('Entertainment'),('Health'),('Shopping'),('Education');

INSERT INTO users (name, email, monthly_income, monthly_budget) VALUES
 ('User 1','user1@example.com',3535,2614),
 ('User 2','user2@example.com',7643,4730),
 ('User 3','user3@example.com',6927,5508);
