import boto3
import pandas as pd
import psycopg2

# AWS S3 connection
s3 = boto3.client('s3')

bucket = "etl-data-lake-abhishek"
file_key = "landing/customers/customers.csv"

# Download file
s3.download_file(bucket, file_key, "customers.csv")

# Read file
df = pd.read_csv("customers.csv")

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="etl_lab",
    user="postgres",
    password="Password@123"
)

cursor = conn.cursor()

# Insert rows
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO staging.customers_stg
        VALUES (%s,%s,%s,%s)
        """,
        (row.customer_id, row.customer_name, row.city, row.signup_date)
    )

conn.commit()
cursor.close()
conn.close()