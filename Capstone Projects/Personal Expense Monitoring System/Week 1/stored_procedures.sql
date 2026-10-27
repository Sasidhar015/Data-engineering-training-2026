USE expense_db;
DROP PROCEDURE IF EXISTS sp_monthly_category_totals;
DELIMITER $$

CREATE PROCEDURE sp_monthly_category_totals(
    IN p_user_id INT,
    IN p_year    INT,
    IN p_month   INT)
BEGIN
    SELECT  c.name                      AS category,
            COUNT(*)                    AS txn_count,
            ROUND(SUM(e.amount), 2)     AS total_spent,
            ROUND(100 * SUM(e.amount) /
                  SUM(SUM(e.amount)) OVER (), 1) AS pct_of_month
    FROM    expenses e
    JOIN    categories c ON c.category_id = e.category_id
    WHERE   e.user_id = p_user_id
      AND   YEAR(e.expense_date)  = p_year
      AND   MONTH(e.expense_date) = p_month
    GROUP BY c.name
    ORDER BY total_spent DESC;
END$$

DELIMITER ;

CALL sp_monthly_category_totals(1, 2026, 4);
