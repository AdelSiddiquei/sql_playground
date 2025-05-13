import psycopg

# Connect to the PostgreSQL database
conn = psycopg.connect(
    dbname="sandbox_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
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