SET search_path TO fashion_db;

-- Case 7: Running Total Monthly Revenue
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month_date,
    	TO_CHAR(o.order_date, 'Mon') AS month,
        SUM(o.quantity * p.price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY 1,2
)
SELECT
    month,
    revenue,
    SUM(revenue) OVER (ORDER BY month) AS running_total_revenue
FROM monthly_revenue
ORDER BY month;

-- Case 8: Month-over-Month Growth
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(o.quantity * p.price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY 1
)
SELECT
    month AS month_date,
	TO_CHAR(month, 'Mon') AS month,
    revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_delta,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month)) 
        / NULLIF(LAG(revenue) OVER (ORDER BY month), 0) * 100,
        2
    ) AS growth_percent
FROM monthly_revenue
ORDER BY 1,2;

-- Case 9: Monthly Customer Ranking by Spending
WITH customer_monthly AS (
    SELECT
        c.customer_id,
        c.customer_name,
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(o.quantity * p.price) AS monthly_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name, month
)
SELECT
    customer_id,
    customer_name,
    month AS month_date,
	TO_CHAR(month, 'Mon') AS month,
    monthly_spent,
    RANK() OVER (PARTITION BY month ORDER BY monthly_spent DESC) AS monthly_rank
FROM customer_monthly
ORDER BY month_date, monthly_rank;