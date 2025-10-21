# Create two tables in database
import sqlite3
connection = sqlite3.connect('university.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE department(deptno integer primary key, deptname text)')
cursor.execute('CREATE TABLE students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references department(deptno))')
connection.commit()
cursor.close()
connection.close()