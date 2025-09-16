import random
from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

fake = Faker('en_IN')
random.seed(42)
Faker.seed(42)
np.random.seed(42)

NUM_RECORDS = 10000

# Locations
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"]
states = ["Maharashtra", "Delhi", "Karnataka", "Telangana", "Tamil Nadu", "West Bengal", "Maharashtra", "Gujarat"]

locations = [{
    "location_id": i+1,
    "latitude": float(fake.latitude()),
    "longitude": float(fake.longitude()),
    "city": cities[i % len(cities)],
    "region": states[i % len(states)],
    "created_at": fake.date_time_between(start_date="-3y", end_date="now")
} for i in range(NUM_RECORDS)]

# Users
def unique_indian_phones(n): return [f"+91{9000000000 + i}" for i in range(n)]
emails = [fake.unique.email() for _ in range(NUM_RECORDS)]
phones = unique_indian_phones(NUM_RECORDS)

users = []
for i in range(NUM_RECORDS):
    user_type = random.choice(["Rider", "Driver"])
    first, last = fake.first_name(), fake.last_name()
    users.append({
        "user_id": i+1,
        "first_name": first,
        "last_name": last,
        "email": emails[i],
        "phone_number": phones[i],
        "user_type": user_type,
        "created_at": fake.date_time_between(start_date="-3y", end_date="now"),
        "updated_at": datetime.now(),
        "location_id": random.choice(locations)["location_id"]
    })

# Vehicle data categorized by type
vehicle_data = {
    "Car": {
        "makes": ["Maruti", "Toyota", "Hyundai", "Tata", "Honda"],
        "models": ["Swift", "Dzire", "Innova", "WagonR", "i20", "Ertiga"]
    },
    "Bike": {
        "makes": ["Hero", "Bajaj", "TVS", "Royal Enfield", "Honda"],
        "models": ["Splendor", "Pulsar", "Apache", "Classic 350", "Activa"]
    },
    "Auto": {
        "makes": ["Bajaj", "TVS", "Piaggio"],
        "models": ["RE", "King", "Ape"]
    }
}

vehicle_types = ["UberX", "UberPool", "UberBlack"]
vehicle_categories = list(vehicle_data.keys())

drivers = [u for u in users if u["user_type"] == "Driver"]
vehicles = []

for i, driver in enumerate(drivers):
    category = random.choice(vehicle_categories)
    make = random.choice(vehicle_data[category]["makes"])
    model = random.choice(vehicle_data[category]["models"])
    
    vehicles.append({
        "vehicle_id": i+1,
        "driver_id": driver["user_id"],
        "make": make,
        "model": model,
        "year": random.randint(2015, 2023),
        "license_plate": f"MH{random.randint(10,99)}AB{random.randint(1000,9999)}",
        "vehicle_type": random.choice(vehicle_types),
        "vehicle_category": category,
        "capacity": random.randint(1, 6) if category != "Bike" else 2,  # Bikes usually 2-seaters
        "created_at": fake.date_time_between(start_date="-3y", end_date="now")
    })


# Trips
riders = [u for u in users if u["user_type"] == "Rider"]
trips = []
for i in range(NUM_RECORDS):
    driver = random.choice(drivers)
    rider = random.choice(riders)
    start_loc = random.choice(locations)
    end_loc = random.choice(locations)
    while end_loc["location_id"] == start_loc["location_id"]:
        end_loc = random.choice(locations)
    start_time = fake.date_time_between(start_date="-2y", end_date="now")
    end_time = start_time + timedelta(minutes=random.randint(5, 45))
    fare = round(random.uniform(50, 800), 2)
    trips.append({
        "trip_id": i+1,
        "user_id": rider["user_id"],
        "driver_id": driver["user_id"],
        "start_location_id": start_loc["location_id"],
        "end_location_id": end_loc["location_id"],
        "start_time": start_time,
        "end_time": end_time,
        "trip_type": random.choice(vehicle_types),
        "fare": fare,
        "distance_km": round(random.uniform(1, 20), 2),
        "rating": round(random.uniform(3.5, 5.0), 2),
        "status": random.choices(["Completed", "Cancelled", "No Show"], weights=[85, 10, 5])[0]
    })

# Payments
payment_methods = ['Credit Card', 'Cash', 'PayPal', 'UPI', 'Paytm']
payment_statuses = ['Completed', 'Pending', 'Failed']
payments = []
for trip in trips:
    payments.append({
        "payment_id": trip["trip_id"],
        "trip_id": trip["trip_id"],
        "amount": trip["fare"],
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choices(payment_statuses, weights=[0.9, 0.07, 0.03])[0],
        "payment_date": trip["end_time"]
    })

# Promotions
promo_trip_types = ['["UberX"]', '["UberPool"]', '["UberBlack"]', '["UberX", "UberPool"]']
promotions = []
for i in range(100):
    start = fake.date_time_between(start_date="-1y", end_date="-1d")
    end = start + timedelta(days=random.randint(7, 90))
    promotions.append({
        "promotion_id": i+1,
        "promo_code": f"INDIA{random.randint(1000,9999)}",
        "discount_percentage": round(random.uniform(5, 30), 2),
        "valid_from": start,
        "valid_until": end,
        "applies_to_trip_types": random.choice(promo_trip_types)
    })

# Driver Performance
performance = []
for driver in drivers:
    trip_count = random.randint(100, 1000)
    performance.append({
        "performance_id": driver["user_id"],
        "driver_id": driver["user_id"],
        "trip_count": trip_count,
        "average_rating": round(random.uniform(3.8, 5.0), 2),
        "cancellation_rate": round(random.uniform(0.0, 0.15), 2),
        "complaints_count": random.randint(0, 20),
        "created_at": fake.date_time_between(start_date="-1y", end_date="now")
    })

# Surge Pricing
surge_pricing = []
for i in range(100):
    start = fake.date_time_between(start_date="-1y", end_date="now")
    end = start + timedelta(hours=random.randint(1, 6))
    surge_pricing.append({
        "surge_id": i+1,
        "start_time": start,
        "end_time": end,
        "surge_multiplier": round(random.uniform(1.2, 3.0), 2),
        "location_id": random.choice(locations)["location_id"],
        "created_at": fake.date_time_between(start_date=start, end_date=end)
    })

# Save all datasets
output_dir = "uber_clone_india_data"
os.makedirs(output_dir, exist_ok=True)

pd.DataFrame(locations).to_csv(f"{output_dir}/locations.csv", index=False)
pd.DataFrame(users).to_csv(f"{output_dir}/users.csv", index=False)
pd.DataFrame(vehicles).to_csv(f"{output_dir}/vehicles.csv", index=False)
pd.DataFrame(trips).to_csv(f"{output_dir}/trips.csv", index=False)
pd.DataFrame(payments).to_csv(f"{output_dir}/payments.csv", index=False)
pd.DataFrame(promotions).to_csv(f"{output_dir}/promotions.csv", index=False)
pd.DataFrame(performance).to_csv(f"{output_dir}/driver_performance.csv", index=False)
pd.DataFrame(surge_pricing).to_csv(f"{output_dir}/surge_pricing.csv", index=False)

print("✅ All India-specific Uber clone data saved in 'uber_clone_india_data'")