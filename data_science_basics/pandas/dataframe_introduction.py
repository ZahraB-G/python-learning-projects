# DataFrame is a tabular data structure with rows and columns.(2-dimension)
# Similar to excel spreadsheet
import pandas as pd
# Create a dataframe
employees = {'Name':['Austin','Jen','Tom'],'Age':[25, 43, 56]}
df = pd.DataFrame(data=employees, index=['Employee 1','Employee 2','Employee 3'])
print('Prnt the data\n',df)
print('===========================================')
# Accessing data in dataframe
print('Access the information for the Employee 1\n',df.loc['Employee 1'])
print('Access the information for the Employee 2\n',df.iloc[2])
print('Accessing all the names \n',df['Name'])
print('===========================================')
# Adding new column
df['Job'] = ['Consultant','Designer','Accountant']
print('Print the new Dataframe\n',df)
print('===========================================')
# Adding new rows
new_df = pd.DataFrame(data = [{'Name':'Sandy','Age':'30','Job':'Developer'}], index=['Employee 4'])
df = pd.concat([df,new_df])
print('Print the new Dataframe\n',df)
print('===========================================')
