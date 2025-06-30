from faker import Faker
import pandas as pd
import random

# Initialize the Faker instance
fake = Faker()

# Product categories and subcategories
categories = ["Electronics", "Furniture", "Clothing", "Home Goods", "Toys", "Books"]
subcategory_mapping = {
    "Electronics": ["Smartphones", "Laptops", "Tablets", "Headphones"],
    "Furniture": ["Sofas", "Chairs", "Tables", "Beds"],
    "Clothing": ["Shirts", "Pants", "Jackets", "Shoes"],
    "Home Goods": ["Kitchenware", "Bedding", "Lighting", "Decor"],
    "Toys": ["Action Figures", "Dolls", "Board Games", "Puzzles"],
    "Books": ["Fiction", "Non-fiction", "Comics", "Children's"]
}

# List to hold the generated product data
product_data = []

# Generate 1000 fake product records
for i in range(1, 1001):
    category = fake.random_element(elements=categories)
    subcategory = fake.random_element(elements=subcategory_mapping[category])
    unit_price = round(random.uniform(10, 1000), 2)  # Random price between $10 and $1000
    cogs = round(unit_price * random.uniform(0.4, 0.7), 2)  # COGS is typically 40-70% of unit price
    
    product = {
        "product_id": f"PROD-{i:03d}",  # Format product ID as PROD-001, PROD-002, ...
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),  # Random product name
        "category": category,
        "subcategory": subcategory,
        "unit_price": unit_price,
        "cogs": cogs
    }
    product_data.append(product)

# Create a DataFrame from the generated product data
product_df = pd.DataFrame(product_data)

# Display the first 5 rows of the product dataset
print(product_df.head())

# Optionally, save the product data to a CSV file
product_df.to_csv("costco_product_data.csv", index=False)