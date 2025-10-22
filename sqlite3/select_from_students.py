# Show the values in the students table
import sqlite3
connection = sqlite3.connect('./sqlite3/university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM students')

tuples = rows.fetchall()
for item in tuples:
    print(item[0], item[1], item[2], item[3])
cursor.close()
connection.close()