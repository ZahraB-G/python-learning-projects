# Find all Customers and their Accounts
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM Customers C')
tuples = rows.fetchall()
for item in tuples:
    print(item)
cursor.close()
connection.close()
