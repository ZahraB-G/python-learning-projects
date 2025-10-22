# Find number of 'ECE' Students residing in each city
import sqlite3
connection = sqlite3.connect('./sqlite3/university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT city, COUNT(*)  FROM students WHERE deptno in (SELECT deptno FROM department WHERE deptname = "ECE") GROUP BY city ORDER BY COUNT(*)')
tuples = rows.fetchall()
for item in tuples:
    print(item[0],item[1])
cursor.close()
connection.close()