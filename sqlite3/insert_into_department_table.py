# Insert the hardcoded info into the department name
import sqlite3
connection = sqlite3.connect('./sqlite3/university.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO department values(10, "CSE")')
cursor.execute('INSERT INTO department values(20, "ECE")')
cursor.execute('INSERT INTO department values(30, "Civil")')
cursor.execute('INSERT INTO department values(40, "Mech")')
connection.commit()
cursor.close()
connection.close()