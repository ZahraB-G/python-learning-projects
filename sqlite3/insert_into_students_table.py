# Insert to student table via the keyboard
import sqlite3
connection = sqlite3.connect('./sqlite3/university.db')
cursor = connection.cursor()

for i in range(10):
    roll = int(input('Enter the roll number: '))
    name = input('Enter the student name: ')
    city = input('Enter the city: ')
    deptno = int(input('Enter the department number: '))
    cursor.execute(f'INSERT INTO students VALUES({roll},"{name}", "{city}", {deptno})')
    
connection.commit()
cursor.close()
connection.close()
