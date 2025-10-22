# Insert data into Accounts table
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO Accounts VALUES(101, 110, "Savings", 2500.0)')
cursor.execute('INSERT INTO Accounts VALUES(102, 111, "Checking", 1200.5)')
cursor.execute('INSERT INTO Accounts VALUES(103, 112, "Saving", 1500.0)')
cursor.execute('INSERT INTO Accounts VALUES(104, 113, "Checking",1700.0 )')
connection.commit()
cursor.close()
connection.close()