# Update Department name to "IT" for deptno 50
# Delete Department 50
import sqlite3
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

# Update the department name
cursor.execute('UPDATE department SET deptname = "IT" WHERE deptno=50 ')

# Delete the department 
cursor.execute('DELETE FROM department WHERE deptname="IT" ')

connection.commit()
cursor.close()
connection.close()