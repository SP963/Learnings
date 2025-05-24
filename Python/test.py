import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import uuid

# Constants
num_records = 10000
incident_types = ['Fire', 'Theft', 'Medical']
response_times = np.random.randint(1, 30, size=num_records)  # Response times in minutes
cctv_coverage = np.random.uniform(80, 100, size=num_records)  # Coverage percentage
downtime = np.random.uniform(0, 5, size=num_records)  # Downtime in hours
drill_compliance = np.random.choice([True, False], size=num_records, p=[0.85, 0.15])  # 85% compliance
lost_found_recovery = np.random.uniform(0, 100, size=num_records)  # Recovery percentage

# Generate timestamps
start_date = datetime.now() - timedelta(days=30)
timestamps = [start_date + timedelta(minutes=random.randint(0, 43200)) for _ in range(num_records)]

# Create DataFrame
data = {
    'Unique_ID': [str(uuid.uuid4()) for _ in range(num_records)],  # Unique identifier
    'Timestamp': timestamps,
    'Incident_Type': [random.choice(incident_types) for _ in range(num_records)],
    'Emergency_Response_Time': response_times,
    'CCTV_Coverage': cctv_coverage,
    'CCTV_Downtime': downtime,
    'Safety_Drill_Compliance': drill_compliance,
    'Lost_Found_Recovery': lost_found_recovery
}

df = pd.DataFrame(data)
df.to_csv('ramoji_film_city_security_data.csv', index=False)
