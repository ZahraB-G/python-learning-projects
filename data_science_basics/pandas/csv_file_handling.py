import pandas as pd
richest = pd.read_csv('data_science_basics/pandas/top_100_richest.csv',usecols=['name'])
print(richest.dtypes)
# print(richest)
print(richest.head()) # returns the first 5 rows by default
print('==================================================================================')
print(richest.head(10)) # returns the first 10 rows
print('==================================================================================')
print(richest.tail(10))
print('==================================================================================')
print(richest.sort_values('name'))
