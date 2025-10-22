# Create Customer Table
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE customers(cust_id integer primary key, name text, address text, email text)')
connection.commit()
cursor.close()
connection.close()
