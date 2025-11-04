import pandas as pd
cols = ['Series_Title', 'IMDB_Rating', 'No_of_Votes','Gross','Released_Year', 'Genre']
movies = pd.read_csv('advanced/pandas/imdb_top_1000.csv',usecols=cols)
# Find the lowest scored movie with the lowest amount of votes
print('The lowest scored movie with the lowest amount of votes is\n',movies.nsmallest(n=1,columns=['IMDB_Rating','No_of_Votes']))
# Find the highest scored movie with the highest amount of votes
print('The highest scored movie with the highest amount of votes is\n',movies.nlargest(n=1,columns=['IMDB_Rating','No_of_Votes']))
# Find the top 5 genres
print('5 Top Genres',movies.value_counts('Genre').head(5))
