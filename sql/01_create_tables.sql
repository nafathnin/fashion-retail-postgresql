SET SEARCH_PATH TO fashion_db;

------------------------------------------- STRUKTUR DATASET

-- Table Customers
CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
	customer_name TEXT,
	city TEXT,
	signup_date DATE
);

-- Table Products
CREATE TABLE products(
	product_id INT PRIMARY KEY,
	product_name TEXT UNIQUE NOT NULL,
	category TEXT,
	price NUMERIC
);

-- Table Orders
CREATE TABLE orders(
	order_id INT PRIMARY KEY,
	customer_id INT,
	product_id INT,
	quantity INT,
	order_date DATE
);

------------------------------------------- ERD (Entity Relationship Diagram)

-- Relation One-to-Many from customers & orders
ALTER TABLE orders 
ADD CONSTRAINT fk_customer_order
FOREIGN KEY(customer_id)
REFERENCES customers(customer_id);

-- Relation One-to-Many from products & orders
ALTER TABLE orders 
ADD CONSTRAINT fk_product_order
FOREIGN KEY(product_id)
REFERENCES products(product_id);

-- SET NOT NULL
ALTER TABLE customers
ALTER COLUMN customer_name SET NOT NULL,
ALTER COLUMN city SET NOT NULL,
ALTER COLUMN signup_date SET NOT NULL;

ALTER TABLE orders
ALTER COLUMN quantity SET NOT NULL,
ALTER COLUMN order_date SET NOT NULL;

ALTER TABLE products
ALTER COLUMN product_name SET NOT NULL,
ALTER COLUMN category SET NOT NULL,
ALTER COLUMN price SET NOT NULL;

-- Import Table using pgAdmin

-- Quick sanity checks
SELECT COUNT(*) FROM orders;
SELECT MIN(order_date), MAX(order_date) FROM orders;
SELECT COUNT(DISTINCT customer_id) FROM orders;
SELECT category, COUNT(*) FROM products GROUP BY category;