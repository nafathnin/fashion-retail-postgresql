# 🛍️ Fashion Retail Sales Analytics — PostgreSQL Project

This project presents an end-to-end SQL analysis of a synthetic Fashion Retail dataset generated using Python (Faker) and analyzed using PostgreSQL.  

The goal is to demonstrate practical SQL skills used in real business scenarios:
sales performance analysis, customer insights, product profitability, and growth metrics.

---

## 📌 Project Overview

This project simulates a retail business environment with:
- **450 customers**
- **60 products**
- **6,000 sales transactions**
- **1 year of sales data (18 Nov 2024 - 18 Dec 2025)**

The dataset was generated using Python to create realistic patterns of:
- product pricing
- category distribution
- purchasing frequency
- seasonal sales behavior

The analysis answers real business questions using JOINs, CTEs, aggregations, and window functions.

---

## 🗂️ Repository Structure

```text
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_sales_analysis.sql
│   ├── 03_customer_analysis.sql
│   ├── 04_product_analysis.sql
│   └── 05_growth_analysis.sql
│
├── python/
│   └── generate_dataset.py
│
├── erd/
│   └── erd.png
│
└── README.md
```

---

## 🧩 Dataset Description

```text
1. customers table
| column        | description                |
| ------------- | -------------------------- |
| customer_id   | Unique customer identifier |
| customer_name | Full name                  |
| city          | Customer city              |
| signup_date   | Date the customer joined   |

2. products table
| column       | description                                       |
| ------------ | ------------------------------------------------- |
| product_id   | Unique product identifier                         |
| product_name | Product name                                      |
| category     | Product category (Tops, Bottoms, Outerwear, etc.) |
| price        | Product price                                     |

3. orders table
| column      | description               |
| ----------- | ------------------------- |
| order_id    | Transaction ID            |
| customer_id | Linked to customers table |
| product_id  | Linked to products table  |
| quantity    | Quantity purchased        |
| order_date  | Transaction date          |
```

---

## 🧱 Entity Relationship Diagram (ERD)(blm FIX)
<img src="erd/erd.png" width="500">

---

## 🎯 Business Questions Answered

Sales Performance
1. What are the total revenue, total orders, and average order value?
2. What does the monthly sales trend look like?

Customer Behavior
3. Who are the top 10 customers based on total spending?
4. What is the average purchase per customer (simple CLV)?

Product Analysis
5. Which products are best-selling (by quantity)?
6. Which product contributes the highest revenue?

Growth Metrics (Window Functions)
7. What is the running total of monthly revenue?
8. What is the MoM growth (delta & growth%)?
9. How are customers ranked based on monthly spending?

---

## 🧠 Key SQL Techniques Used

- JOIN for combining multiple tables
- GROUP BY + aggregations for metrics
- CTE (WITH clause) for cleaner query logic
- WINDOW FUNCTIONS (LAG, SUM OVER) for growth & ranking
- DATE_TRUNC for monthly grouping
- Subqueries for top-N analysis

---

## 📊 Sample Queries

1. Monthly Sales Trend
SELECT
    DATE_TRUNC('month', o.order_date) AS month_date,
    TO_CHAR(o.order_date, 'Mon') AS month,
    SUM(o.quantity * p.price) AS monthly_revenue,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY 1,2
ORDER BY 1,2;

2. Top 10 Customers
SELECT
    c.customer_name,
    SUM(quantity * price) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;

3. Month-over-Month Revenue Growth
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month_date,
	TO_CHAR(month, 'Mon') AS month,
        SUM(o.quantity * p.price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY month
)
SELECT
    month,
    revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_delta,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month)) 
        / NULLIF(LAG(revenue) OVER (ORDER BY month), 0) * 100,
        2
    ) AS growth_percent
FROM monthly_revenue
ORDER BY month;

---

## 📈 Key Insights

- Monthly revenue remained relatively stable, ranging from $40,000 to $50,000 throughout 2025.
- Highest revenue: August 2025 — $49,793.64
- Lowest revenue: February 2025 — $41,655.04
- Monthly orders were consistent (470–525 orders).
- Best-selling products: Flannel Pajama Pants, Straight Jeans, Chelsea Boots
- Top revenue contributors: Wool Coat, Parka Jacket, Trench Coat
- Highest Month-over-Month (MoM) revenue growth: March 2025

---

## 🚀 How to Run This Project

- Clone repository
- Import customers.csv, products.csv, and orders.csv into PostgreSQL
- Run table creation scripts in /sql/01_create_tables.sql
- Run analysis scripts in /sql/
- (Optional) Modify dataset using python/generate_dataset.py

---

## 👩‍💻 Author

Fathnin Nur Azmina
Data Analyst (Entry-Level)
LinkedIn: https://linkedin.com/in/fathninuraz