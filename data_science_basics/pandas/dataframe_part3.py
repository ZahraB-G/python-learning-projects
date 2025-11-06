import pandas as pd
cols = ['Series_Title','IMDB_Rating','No_of_Votes']
movies = pd.read_csv('data_science_basics/pandas/imdb_top_1000.csv',usecols=cols)
movies = pd.DataFrame(data=movies)
print('The top 10 Movies based on rating\n',movies.nlargest(n=10,columns=['IMDB_Rating']))
print('==================================================================================')
print('The bottom 10 Movies based on rating\n',movies.nsmallest(n=10,columns=['IMDB_Rating']))
#print(movies)