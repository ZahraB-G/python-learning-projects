import pandas as pd
cols = ['Series_Title','IMDB_Rating', 'No_of_Votes','Gross','Released_Year','Genre']
movies = pd.read_csv('data_science_basics/pandas/imdb_top_1000.csv',usecols=cols)
print('info() method gives a lot of information such as ',movies.info())
# Convert Grocc into an integer so it can be as numric data
movies['Gross'] = movies['Gross'].str.replace(',','')
movies['Gross'].fillna(0,inplace=True)
movies['Gross']=movies['Gross'].astype('int64')

print(movies.count())