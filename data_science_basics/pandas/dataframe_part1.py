import pandas as pd
richest = pd.read_csv('data_science_basics/pandas/top_100_richest.csv')
print('The Shape of richest is ',richest.shape)
print('The number of elements in the dataframe is ',richest.size)
print('The index of the dataframe is ', richest.index)
print('The coloumns of the dataframe is ', richest.columns)