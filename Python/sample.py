import random
import csv

# Generate 355 random numbers between 10,000 and 99,999
random_numbers = [random.randint(2000000,4000000) for _ in range(5680)]

# Save the numbers into a CSV file
csv_file = "random_numbers.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Random Numbers'])  # Add header
    for number in random_numbers:
        writer.writerow([number])

print("CSV file 'random_numbers.csv' has been created.")
