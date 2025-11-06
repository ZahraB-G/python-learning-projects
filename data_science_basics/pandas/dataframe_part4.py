import pandas as pd
movies = pd.read_csv('data_science_basics/pandas/imdb_top_1000.csv').head(3)
movies.drop(columns=['Poster_Link','Certificate','Overview','Runtime'],inplace=True)

print('Remove the three columns from the dataframe\n',movies)
print('==================================================================================')
print(movies.drop([1,2]))