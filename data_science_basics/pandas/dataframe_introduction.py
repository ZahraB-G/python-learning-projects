# DataFrame is a tabular data structure with rows and columns.(2-dimension)
# Similar to excel spreadsheet
import pandas as pd
# Create a dataframe
employees = {'Name':['Austin','Jen','Tom'],'Age':[25, 43, 56]}
df = pd.DataFrame(data=employees)
print(df)