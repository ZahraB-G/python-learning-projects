import pandas as pd
richest = pd.read_csv('data_science_basics/pandas/top_100_richest.csv')
# Selection by Columns
print('Show the all the names\n',richest['name'])
print('==================================================================================')
print(richest[['name','net_worth','age']])
print('==================================================================================')
# Selection by rows
richest_list = pd.read_csv('data_science_basics/pandas/top_100_richest.csv',index_col='name')
print('All the info about Jeff Bezos',richest_list.loc['Jeff Bezos'])
print('==================================================================================')
print('Richest people from Jeff Bezos and Bill Gates\n',richest_list.loc['Jeff Bezos':'Bill Gates',['age','rank']])
print('==================================================================================')
# Filtering is keeping the rows that matches condition
print('Show all the Rich people who are younger than 50 years old\n',richest_list[richest_list['age']<50])
print('==================================================================================')
# Aggregate Functions: reduces a set of values into a single summary value
# Used to summarized and analyze data
# Often used with the groupby() function
# Use aggregative function on whole dataframe
print('Show all the average numeric values\n',richest.mean(numeric_only=True))
print('Show all the min numeric values\n',richest.min(numeric_only=True))
print('Show all the max numeric values\n',richest.max(numeric_only=True))
print('==================================================================================')
# Use aggregate functions on one column
print('Show the average age\n',richest['age'].mean())
print('Show the youngest \n',richest['age'].min())
print('Show the oldest \n',richest['age'].max())
print('==================================================================================')
group = richest.groupby('nationality')
print(group['age'].mean())
