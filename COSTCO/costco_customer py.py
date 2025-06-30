from faker import Faker
import pandas as pd
import random

# Initialize the Faker instance
fake = Faker()

# List of cities in the United States (can be expanded)
us_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington"
]

# List to hold the generated customer data
data = []

# Generate 1000 fake customer records
for i in range(1, 1001):
    customer = {
        "Customer ID": f"CUST-{i:03d}",  # Format ID as CUST-001, CUST-002, ...
        "Name": fake.name(),
        "Segment": fake.random_element(elements=("Consumer", "Corporate", "Home Office")),
        "Country-City": f"United States - {random.choice(us_cities)}",  # Combine country and random city
        "State": fake.state(),
        "Postal Code": fake.zipcode(),
        "Region": fake.random_element(elements=("South", "North", "West", "East", "Central"))  # Added Central
    }
    data.append(customer)

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Display the first 5 rows of the dataset
print(df.head())

# Optionally, save the dataset to a CSV file
df.to_csv("synthetic_costco_customer_data_with_country_city_and_central_region.csv", index=False)
