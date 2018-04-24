import pandas as pd

df = pd.ExcelFile('location/test.xlsx').parse('Sheet1') 
#you could add index_col=0 if there's an index
x=[]
x.append(df['name_of_col'])
