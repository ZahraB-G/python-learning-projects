# Find all Customers and their Accounts
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT C.name, C.address, C.email, A.acc_type, A.balance FROM Customers C JOIN accounts A ON C.cust_id = A.cust_id ORDER BY C.cust_id')
tuples = rows.fetchall()
for item in tuples:
    print(item)
cursor.close()
connection.close()
