# Show the values in the Department table
import sqlite3
connection = sqlite3.connect('university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM department')
tuples = rows.fetchall()
for item in tuples:
    print(f'Department No: {item[0]}, Department Name: {item[1]}')
cursor.close()
connection.close()