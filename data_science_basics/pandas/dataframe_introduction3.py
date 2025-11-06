# Data Cleaning = the process of fixing or removing: incomplete
# incorrect or irrelevent data. ~75% of work done with pandas is data cleaning.
import pandas as pd
df = pd.read_csv('data_science_basics/pandas/top_100_richest.csv')
print(df)
# Drop irrelevent columns
df.drop(columns=['bday'],inplace=True)
print(df)
# Handle missing data
df.dropna(subset=['age'],inplace=True)
df.fillna({'age':'N/A'})
print(df.to_string())
# Fix inconsistance value
df['nationality'] = df['nationality'].replace({'China':'CHINA'})
print(df['nationality'].to_string())
# Standardaize Text
df['nationality']=df['nationality'].str.upper()
print(df)
# Fix data type
df['age']=df['age'].astype('Int64')
print(df)
# Remove duplicate function
df = df.drop_duplicates()
print(df)