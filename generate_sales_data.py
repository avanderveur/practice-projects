# generate_sales_data.py
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Generate synthetic historical sales data
def generate_sales_data(start_date, end_date, num_products, num_customers):
    data = []
    date_generated = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]
    
    for date in date_generated:
        for _ in range(num_products):
            product_id = fake.uuid4()
            customer_id = fake.uuid4()
            quantity_sold = random.randint(1, 100)
            unit_price = round(random.uniform(10, 200), 2)
            total_price = round(quantity_sold * unit_price, 2)

            data.append({
                'Date': date,
                'ProductID': product_id,
                'CustomerID': customer_id,
                'QuantitySold': quantity_sold,
                'UnitPrice': unit_price,
                'TotalPrice': total_price
            })

    df = pd.DataFrame(data)
    return df

# Define the date range for historical data
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate synthetic data for 5 products and 100 customers
sales_data = generate_sales_data(start_date, end_date, num_products=5, num_customers=100)

# Save the synthetic data to a CSV file
sales_data.to_csv('data/historical_sales.csv', index=False)

print("Synthetic historical sales data generated and saved to historical_sales.csv.")
