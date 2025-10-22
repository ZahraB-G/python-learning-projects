# Create Tansaction Table
import sqlite3
connection = sqlite3.connect('./mini_projects/bank_database/bank.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE transactions(trans_id integer primary key, acc_id integer, tran_type text, amount real, date Date, foreign key(acc_id) references accounts(acc_id))')
connection.commit()
cursor.close()
connection.close()