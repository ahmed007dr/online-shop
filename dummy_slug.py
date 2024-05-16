import sqlite3
from faker import Faker
import string
import random

# Connect to the SQLite database
conn = sqlite3.connect('F:\django-5\shop-online\shop\src\db.sqlite3')
cursor = conn.cursor()

# Create a Faker instance
fake = Faker()

# Define a function to generate a fake slug
def generate_fake_slug(length=10):
    # Generate a random string of lowercase letters and digits
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Fetch all rows from the table you want to update
cursor.execute("SELECT id, name FROM products_products")
rows = cursor.fetchall()

# Iterate over the rows and update the slug field
for row in rows:
    # Generate a fake slug
    fake_slug = generate_fake_slug()
    
    # Update the row with the fake slug
    cursor.execute("UPDATE products_products SET slug=? WHERE id=?", (fake_slug, row[0]))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("All slugs updated successfully.")
