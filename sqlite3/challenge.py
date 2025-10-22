# Find 'Civil' Department Students not from 'NY'
import sqlite3
connection = sqlite3.connect('university.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT name FROM students WHERE deptno in(SELECT deptno FROM department WHERE deptname == "Civil") and city != "NY"')
tuples = rows.fetchall()
for item in tuples:
    print(item[0])
cursor.close()
connection.close()
