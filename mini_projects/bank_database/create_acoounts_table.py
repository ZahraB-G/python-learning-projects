# Create Accounts Table
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE Accounts(acc_id integer primary key, cust_id integer, acc_type text, balance real, foreign key(cust_id) references customer(cust_id))')
connection.commit()
cursor.close()
connection.close()