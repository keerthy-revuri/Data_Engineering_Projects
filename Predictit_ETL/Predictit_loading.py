
import psycopg2
import os

def execute_sql_file(sql_file_path, conn):
    # Read the contents of the .sql file
    with open(sql_file_path, 'r') as file:
        sql_statements = file.read()

    # Split the contents into individual SQL statements
    sql_statements = sql_statements.split(';')

    # Remove empty statements and leading/trailing whitespace
    sql_statements = [stmt.strip() for stmt in sql_statements if stmt.strip()]

    # Create a cursor object
    cur = conn.cursor()

    # Execute each SQL statement
    for stmt in sql_statements:
        print(f"Executing SQL statement: {stmt}")
        cur.execute(stmt)
        conn.commit()

    # Close the cursor
    cur.close()

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

# Specify the path to your .sql file
sql_file_path = 'C:/Users/keert/Data_Engineering_Projects/Predictit_ETL/load_script.sql'

# Get the full file path of the current script
current_file_path = os.path.abspath(__file__)
print("Current file path:", current_file_path)

# Execute SQL statements from the .sql file
execute_sql_file(sql_file_path, conn)

# Close the connection
conn.close()

