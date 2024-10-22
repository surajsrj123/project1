


# when you using window authentication then only use pyodbc library
import pyodbc

# Define the connection details
server = 'DESKTOP-G7INU7F\\SQLEXPRESS'  # Server name
database = 'dbt'  # Your database name

# Create a connection object with Windows Authentication (no password needed)
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'Trusted_Connection=yes;'
)

# Create a connection object
conn = pyodbc.connect(conn_str)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example query
cursor.execute('SELECT empname FROM empinfo101')

# Fetch the result
rows = cursor.fetchall()

# Print the result
mydata = []
for row in rows:
    print('id ====>',row[0])
    print('name ====>',row[1])
    print('salary ====>',row[2])
    print('department ====>',row[3])
    item = {
        "id":row[0],
        "name":row[1],
        "salary":row[2],
        "department":row[3],
    }
    mydata.append(item)
print('mydata ==>',mydata)
# Close the connection
cursor.close()
conn.close()