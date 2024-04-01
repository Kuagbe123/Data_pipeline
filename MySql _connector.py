import mysql.connector
from faker import Faker
import random

fake = Faker()

# Generate 100,000 records for customer_data
records = []
for _ in range(100000):
    name = fake.name()
    address = fake.address()
    transaction_activity = random.randint(0, 10000)
    app_preference = random.choice(['Yes', 'No'])
    website_preference = random.choice(['Yes', 'No'])
    email = fake.email()
    records.append((name, address, transaction_activity, app_preference, website_preference, email))

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="O01>6q94",
    database="bank_data"
)

# Create cursor
mycursor = mydb.cursor()

# SQL statement for inserting records into customer_data table
sql = "INSERT INTO customer_data (name, address, transaction_activity, app_preference, website_preference, email) VALUES (%s, %s, %s, %s, %s, %s)"

# Execute the SQL statement with executemany()
mycursor.executemany(sql, records)

# Commit the transaction
mydb.commit()

# Print the number of records inserted
print(mycursor.rowcount, "records inserted.")
