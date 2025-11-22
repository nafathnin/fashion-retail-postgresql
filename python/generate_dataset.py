import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# ============================
# 1. PRODUCT LIST (FROM YOU)
# ============================
products_list = [
    # Tops
    ("Basic Cotton T-Shirt", "Tops", 10, 20),
    ("Oversized T-Shirt", "Tops", 12, 25),
    ("Graphic T-Shirt", "Tops", 15, 30),
    ("Long Sleeve Tee", "Tops", 18, 35),
    ("Casual Blouse", "Tops", 20, 40),
    ("Linen Blouse", "Tops", 25, 45),
    ("Crop Top", "Tops", 10, 18),
    ("Knitted Sweater", "Tops", 25, 45),
    ("Hoodie Pullover", "Tops", 30, 50),
    ("Zip-Up Hoodie", "Tops", 35, 55),

    # Bottoms
    ("Slim Fit Jeans", "Bottoms", 30, 60),
    ("Straight Jeans", "Bottoms", 30, 55),
    ("High-Waist Trousers", "Bottoms", 25, 50),
    ("Jogger Pants", "Bottoms", 20, 40),
    ("Chino Pants", "Bottoms", 25, 45),
    ("Pleated Skirt", "Bottoms", 20, 40),
    ("A-Line Skirt", "Bottoms", 22, 45),
    ("Cargo Pants", "Bottoms", 28, 55),

    # Outerwear
    ("Denim Jacket", "Outerwear", 40, 70),
    ("Bomber Jacket", "Outerwear", 45, 80),
    ("Puffer Jacket", "Outerwear", 60, 120),
    ("Wool Coat", "Outerwear", 80, 150),
    ("Trench Coat", "Outerwear", 75, 130),
    ("Windbreaker", "Outerwear", 35, 65),
    ("Parka Jacket", "Outerwear", 60, 100),

    # Activewear
    ("Training T-Shirt", "Activewear", 15, 30),
    ("Sports Bra", "Activewear", 18, 35),
    ("Running Shorts", "Activewear", 15, 28),
    ("Yoga Leggings", "Activewear", 20, 45),
    ("Gym Joggers", "Activewear", 22, 45),
    ("Active Hoodie", "Activewear", 30, 50),

    # Sleepwear
    ("Cotton Pajama Set", "Sleepwear", 15, 35),
    ("Satin Pajama Set", "Sleepwear", 20, 45),
    ("Sleep Shirt", "Sleepwear", 12, 25),
    ("Bath Robe", "Sleepwear", 25, 50),
    ("Flannel Pajama Pants", "Sleepwear", 15, 30),

    # Accessories
    ("Canvas Tote Bag", "Accessories", 10, 25),
    ("Mini Shoulder Bag", "Accessories", 15, 35),
    ("Leather Belt", "Accessories", 18, 40),
    ("Wool Scarf", "Accessories", 12, 28),
    ("Beanie Hat", "Accessories", 10, 20),
    ("Baseball Cap", "Accessories", 10, 20),
    ("Ankle Socks", "Accessories", 3, 7),
    ("Crew Socks", "Accessories", 4, 8),

    # Footwear
    ("White Sneakers", "Footwear", 30, 65),
    ("Running Shoes", "Footwear", 35, 80),
    ("Slip-On Shoes", "Footwear", 25, 50),
    ("Chelsea Boots", "Footwear", 50, 100),
    ("Sandals", "Footwear", 15, 35),
    ("Chunky Sneakers", "Footwear", 40, 85),

    # Additional SKUs
    ("Ribbed Tank Top", "Tops", 10, 18),
    ("V-Neck Sweater", "Tops", 25, 45),
    ("Polo Shirt", "Tops", 15, 35),
    ("Linen Shorts", "Bottoms", 18, 35),
    ("Wide-Leg Pants", "Bottoms", 25, 50),
    ("Midi Skirt", "Bottoms", 20, 40),
    ("Knitted Cardigan", "Outerwear", 28, 55),
    ("Lightweight Jacket", "Outerwear", 30, 60),
    ("Sports Socks", "Accessories", 5, 10),
    ("Crossbody Bag", "Accessories", 20, 40),
]

# ============================
# 2. PRODUCTS TABLE
# ============================
products = []
for i, (name, category, min_price, max_price) in enumerate(products_list, start=1):
    products.append([
        i,
        name,
        category,
        round(random.uniform(min_price, max_price), 2)
    ])

df_products = pd.DataFrame(products, columns=["product_id", "product_name", "category", "price"])


# ============================
# 3. CUSTOMERS TABLE
# ============================
num_customers = 450
customers = []

start_date = datetime(2018, 5, 6)
end_date = datetime(2025, 11, 18, 23, 59, 59)

for i in range(1, num_customers + 1):
    customers.append([
        i,
        fake.name(),
        fake.city(),
        fake.date_between(start_date=start_date, end_date=end_date)
    ])

df_customers = pd.DataFrame(customers, columns=["customer_id", "customer_name", "city", "signup_date"])


# ============================
# 4. ORDERS TABLE (6,000 SALES)
# ============================
num_orders = 6000
orders = []

start_date = datetime(2024, 11, 18)
end_date = datetime(2025, 11, 18, 23, 59, 59)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

for order_id in range(1, num_orders + 1):
    product = random.choice(products)
    customer = random.choice(customers)

    orders.append([
        order_id,
        customer[0],
        product[0],
        random.randint(1, 4),  # quantity
        random_date(start_date, end_date)
    ])

df_orders = pd.DataFrame(orders, columns=[
    "order_id",
    "customer_id",
    "product_id",
    "quantity",
    "order_date"
])

# ============================
# SAVE TO CSV
# ============================
df_products.to_csv("products.csv", index=False)
df_customers.to_csv("customers.csv", index=False)
df_orders.to_csv("orders.csv", index=False)

print("✔ Dataset generated successfully!")
print("products.csv, customers.csv, orders.csv created.")
