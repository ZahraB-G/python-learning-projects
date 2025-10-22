# Find Student Names from 'CSE' Department
import sqlite3
connection = sqlite3.connect('university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT name FROM students where deptno in (SELECT deptno FROM department WHERE deptname == "CSE")')
tuples = rows.fetchall()
for item in tuples:
    print(item[0])
cursor.close()
connection.close()