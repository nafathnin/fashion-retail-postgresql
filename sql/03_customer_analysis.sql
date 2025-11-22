SET search_path TO fashion_db;

-- Case 3: Top 10 Customers by Total Spending
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.quantity * p.price) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- Case 4: Average Spending per Customer (Simple CLV)
WITH customer_total AS (
    SELECT
        c.customer_id,
        SUM(o.quantity * p.price) AS total_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id
)
SELECT
    AVG(total_spent) AS avg_customer_lifetime_value
FROM customer_total;