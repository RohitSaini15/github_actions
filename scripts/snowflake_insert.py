import snowflake.connector
import os

# Snowflake connection details
account = os.environ['SNOWFLAKE_ACCOUNT']
user = os.environ['SNOWFLAKE_USER']
password = os.environ['SNOWFLAKE_PASSWORD']
warehouse = os.environ['SNOWFLAKE_WAREHOUSE']
database = os.environ['SNOWFLAKE_DATABASE']
schema = os.environ['SNOWFLAKE_SCHEMA']

# Connection to Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# Create a cursor object
cursor = conn.cursor()

# Replace with your actual INSERT query
insert_query = """
    INSERT INTO your_table (NAME,PASSWORD)
    VALUES (%s, %s, %s)
"""

# Replace with the actual values you want to insert
values = ('jigyasa', 'admin123',)

# Execute the INSERT query
cursor.execute(insert_query, values)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
