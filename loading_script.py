from pg_utils import csv_to_pg_loader as loader

loader = loader.PostgresCSVLoader()

csv_files = [
    "data/brands.csv",
    "data/categories.csv",  # Can change this script for any list of csv's that are named appropriately
    "data/customers.csv",
    "data/order_items.csv",
    "data/staffs.csv",
    "data/stocks.csv",
    "data/stores.csv",
]

for file in csv_files:
    loader.process_csv(file)
loader.close()
