
# when you have user name and passwod then only you can use pymssql library

import pymssql

# Define the connection details
server = 'DESKTOP-G7INU7F\\SQLEXPRESS'  # Server name (double backslash needed)
database = 'dbt'  # Your database name
username = 'your_sql_username'  # SQL Server username (e.g., 'sa')
password = 'your_sql_password'  # SQL Server password

try:
    # Create a connection object
    conn = pymssql.connect(server, username, password, database)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example query
    cursor.execute('SELECT * FROM empinfo101')

    # Fetch the result
    rows = cursor.fetchall()

    # Print the result
    for row in rows:
        print(row)

except pymssql.InterfaceError as ie:
    print("Error connecting to the server:", ie)
except pymssql.DatabaseError as de:
    print("Database error occurred:", de)
finally:
    # Ensure the connection is closed
    if cursor:
        cursor.close()
    if conn:
        conn.close()
