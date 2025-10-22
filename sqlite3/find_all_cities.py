# Find all the cities where Students are living.
import sqlite3
connection = sqlite3.connect('./sqlite3/university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT DISTINCT CITY FROM STUDENTS')     
tuples = rows.fetchall()
for item in tuples:
    print(item[0])
cursor.close()
connection.close()