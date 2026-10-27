USE expense_db;

INSERT INTO expenses (user_id, category_id, amount, expense_date, description, payment_method)
VALUES (1, 1, 54.30, '2026-04-03', 'Weekly groceries', 'UPI'),
       (1, 2, 1060.50, '2026-04-01', 'April rent', 'Debit Card'),
       (1, 5, 32.00, '2026-04-09', 'Dinner out', 'Credit Card'),
       (2, 4, 18.75, '2026-04-04', 'Cab ride', 'UPI'),
       (2, 1, 61.10, '2026-04-12', 'Groceries', 'Cash'),
       (2, 2, 2290.00, '2026-04-01', 'April rent', 'Debit Card'),
       (1, 1, 47.80, '2026-05-06', 'Groceries', 'UPI'),
       (1, 2, 1060.50, '2026-05-01', 'May rent', 'Debit Card');

SELECT e.expense_id, u.name, c.name AS category, e.amount, e.expense_date
FROM expenses e
JOIN users u      ON u.user_id = e.user_id
JOIN categories c ON c.category_id = e.category_id
WHERE e.user_id = 1
ORDER BY e.expense_date DESC;

UPDATE expenses SET amount = 58.00, description = 'Weekly groceries (corrected)'
WHERE expense_id = 1;

DELETE FROM expenses WHERE expense_id = 7;

SELECT user_id, DATE_FORMAT(expense_date,'%Y-%m') AS month, SUM(amount) AS total
FROM expenses GROUP BY user_id, month ORDER BY user_id, month;
