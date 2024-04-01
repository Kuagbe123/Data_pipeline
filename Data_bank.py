from faker import Faker
import random

fake = Faker()

# Generate demographic data
def generate_demographics():
    name = fake.name()
    address = fake.address()
    return name, address

# Generate transaction activity data
def generate_transaction_activity():
    return random.randint(0, 10000)  # Assuming transaction activity is represented as a number

# Generate customer preferences data
def generate_customer_preferences():
    app_preference = random.choice(['Yes', 'No'])
    website_preference = random.choice(['Yes', 'No'])
    return app_preference, website_preference

# Generate communication methods data
def generate_communication_methods():
    email = fake.email()
    return email

# Generate 100,000 records
records = []
for _ in range(100000):
    demographics = generate_demographics()
    transaction_activity = generate_transaction_activity()
    customer_preferences = generate_customer_preferences()
    communication_methods = generate_communication_methods()
    records.append((*demographics, transaction_activity, *customer_preferences, communication_methods))

# Display sample record
print(records[0])
