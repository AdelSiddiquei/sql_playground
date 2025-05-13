import os
from dotenv import load_dotenv
import psycopg

# Load environment variables from .env file
load_dotenv()

# Access the variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


# Connect to the PostgreSQL database
conn = psycopg.connect(
    dbname=DB_NAME,
    user= DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM coffee_sales_2024 LIMIT 5;")

# Fetch results
rows = cur.fetchall()
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()
