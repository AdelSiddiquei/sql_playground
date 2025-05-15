import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

'''Needs Update for also choosing data types'''

class PostgresCSVLoader:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Connect to PostgreSQL database using credentials from .env
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DB"),
        )

        # Use autocommit so that each statement is committed without conn.commit()
        self.conn.autocommit = True

        # Create a cursor to execute SQL queries
        self.cursor = self.conn.cursor()

    def get_table_name(self, csv_path):
        # Find filename to use as the table name
        return os.path.splitext(os.path.basename(csv_path))[0]

    def create_table(self, csv_path, table_name=None):
        # Load CSV into a pandas DataFrame
        df = pd.read_csv(csv_path)

        # Use the provided table name or infer from the CSV filename
        table_name = table_name or self.get_table_name(csv_path)

        # Generate a SQL string with all column names as TEXT
        columns = ", ".join([f'"{col}" TEXT' for col in df.columns])

        # Construct CREATE TABLE SQL query
        create_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns});'

        # Execute query
        self.cursor.execute(create_query)
        print(f"Table '{table_name}' created or already exists.")

        # Return the DataFrame and table name for use in the next step
        return df, table_name

    def load_data(self, df, table_name):
        # Iterate over each row of df
        for _, row in df.iterrows():
            # Put placeholders and format column names for the SQL query
            placeholders = ", ".join(["%s"] * len(row))
            columns = ", ".join([f'"{col}"' for col in df.columns])

            # Construct INSERT SQL query
            insert_query = (
                f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders});'
            )

            # Execute INSERT query with row's values
            self.cursor.execute(insert_query, tuple(row))

        print(f"Data loaded into '{table_name}' successfully.")

    def process_csv(self, csv_path):                #need to update to also allow manual col names and data types
        # Full csv to pg table pipelin.
        df, table_name = self.create_table(csv_path)
        self.load_data(df, table_name)

    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.conn.close()
