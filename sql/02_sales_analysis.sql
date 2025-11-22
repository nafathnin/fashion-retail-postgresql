SET search_path TO fashion_db;

-- Case 1: Total revenue, total order, dan average order value
SELECT
    SUM(o.quantity * p.price) AS total_revenue,
    COUNT(o.order_id) AS total_order,
    AVG(o.quantity * p.price) AS average_order_value
FROM orders o
JOIN products p ON o.product_id = p.product_id;

-- Case 2: Monthly Sales Trend (Revenue per Month)
SELECT
    DATE_TRUNC('month', o.order_date) AS month_date,
    TO_CHAR(o.order_date, 'Mon') AS month,
    SUM(o.quantity * p.price) AS monthly_revenue,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY 1,2
ORDER BY 1,2;