import pandas as pd
import random
from faker import Faker
import numpy as np

fake = Faker()
Faker.seed(0)
random.seed(0)
np.random.seed(0)

# Constants
num_records = 1000
product_categories = {
    "Electronics": ["Wireless Mouse", "Bluetooth Speaker", "Laptop Stand"],
    "Home": ["Vacuum Cleaner", "Air Purifier", "LED Lamp"],
    "Fitness": ["Yoga Mat", "Dumbbells", "Treadmill"],
    "Fashion": ["Sneakers", "Jacket", "Wristwatch"]
}

regions = {
    "USA": ["North-East", "South-West", "Mid-West", "West Coast"],
    "UK": ["England", "Scotland", "Wales"],
    "India": ["North", "South", "East", "West"]
}

customer_segments = ["Regular", "Premium", "Enterprise"]
payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash on Delivery", "Net Banking"]
order_statuses = ["Completed", "Cancelled", "Returned"]

def generate_product():
    category = random.choice(list(product_categories.keys()))
    sub_category = category  # For simplicity
    product_name = random.choice(product_categories[category])
    unit_price = round(random.uniform(10, 500), 2)
    return category, sub_category, product_name, unit_price

data = []

for i in range(num_records):
    order_id = f"O{1000+i}"
    order_date = fake.date_between(start_date='-6M', end_date='today')
    customer_id = f"C{random.randint(100, 999)}"
    customer_name = fake.name()
    customer_segment = random.choice(customer_segments)

    country = random.choice(list(regions.keys()))
    region = random.choice(regions[country])

    product_id = f"P{random.randint(100, 999)}"
    category, sub_category, product_name, unit_price = generate_product()
    quantity_sold = random.randint(1, 5)
    total_sales_amount = round(quantity_sold * unit_price, 2)
    discount_amount = round(random.uniform(0, 0.2) * total_sales_amount, 2)
    net_sales_amount = round(total_sales_amount - discount_amount, 2)

    payment_method = random.choice(payment_methods)
    order_status = random.choices(order_statuses, weights=[0.85, 0.1, 0.05])[0]

    data.append([
        order_id, order_date, customer_id, customer_name, customer_segment,
        region, country, product_id, product_name, category, sub_category,
        quantity_sold, unit_price, total_sales_amount, discount_amount,
        net_sales_amount, payment_method, order_status
    ])

columns = [
    "Order_ID", "Order_Date", "Customer_ID", "Customer_Name", "Customer_Segment",
    "Region", "Country", "Product_ID", "Product_Name", "Category", "Sub_Category",
    "Quantity_Sold", "Unit_Price", "Total_Sales_Amount", "Discount_Amount",
    "Net_Sales_Amount", "Payment_Method", "Order_Status"
]

df_sales = pd.DataFrame(data, columns=columns)

# Save to Excel
df_sales.to_excel("Sales_Data_1000_Records.xlsx", index=False)
print("Excel file 'Sales_Data_1000_Records.xlsx' has been created.")
