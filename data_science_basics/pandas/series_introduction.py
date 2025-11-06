# Series is Pandas 1-dimensional labeled array that can hold any type of data
# Think of it as single column in a spreadsheet (1-Dimentional)
import pandas as pd
courses = ['Math','Pysic','Chemistry']
grades = ['a','b','x']
# Creating Series
series = pd.Series(data=courses, index=grades)
# Accessing value
print('The Value of the index == a is ',series['a'])
print('The Value of the index == b is ',series.loc['b'])
print('The Value of the index == 2 is ',series.iloc[2])
# Filtering values
data = [100, 200, 300, 400, 500, 600]
series = pd.Series(data)
print('Print the values more than 200\n',series[series>200])
