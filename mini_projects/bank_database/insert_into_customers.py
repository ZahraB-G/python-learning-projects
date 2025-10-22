# Insert data into Customers table
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO Customers VALUES(110, "Ana", "NY", "Ana@gmail.com")')
cursor.execute('INSERT INTO Customers VALUES(111, "Ale", "TX", "Ale@gmail.com")')
cursor.execute('INSERT INTO Customers VALUES(112, "Ron", "CA", "Ron@gmail.com")')
cursor.execute('INSERT INTO Customers VALUES(113, "Yara", "AZ", "Yara@gmail.com")')
connection.commit()
cursor.close()
connection.close()