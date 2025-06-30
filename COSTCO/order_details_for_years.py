import random
import csv
from datetime import datetime, timedelta

# Function to generate random date
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Generate order data for each year from 2020 to 2025
for year in range(2020, 2026):  # Loop through years 2020 to 2025
    order_data = []
    order_id = 1  # Starting Order ID for each year
    customers = [f'CUST-{str(i).zfill(3)}' for i in range(1, 1001)]  # Customer IDs from CUST-001 to CUST-1000
    products = [f'PROD-{str(i).zfill(3)}' for i in range(1, 101)]  # Product IDs from PROD-001 to PROD-100
    ship_modes = ['First Class', 'Second Class', 'Third Class', 'Same Day']

    # Date range for the orders in the current year
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    for _ in range(1000):  # Loop to generate 1000 rows of data
        order_date = random_date(start_date, end_date)
        ship_date = order_date + timedelta(days=random.randint(1, 7))  # Ship date 1 to 7 days after order date
        ship_mode = random.choice(ship_modes)

        customer_id = random.choice(customers)
        product_id = random.choice(products)
        quantity = random.randint(1, 10)  # Quantity between 1 and 10
        discount = random.choice([0,0.1,0.2])  # Discount options 

        order_data.append([f'ORD-{str(order_id).zfill(3)}', 
                           order_date.strftime('%Y-%m-%d'), 
                           ship_date.strftime('%Y-%m-%d'),
                           ship_mode, 
                           customer_id, 
                           product_id, 
                           quantity, 
                           discount])
        order_id += 1  # Increment order ID

    # Write the generated data to a CSV file for the current year
    header = ['Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Product ID', 'Quantity', 'Discount']
    filename = f'order_details_{year}.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header row
        writer.writerows(order_data)  # Write all order data

    print(f"CSV file 'order_details_{year}.csv' has been generated.")
