import pandas as pd
import numpy as np

#Import and read file
df = pd.read_csv('C:/Users/EriksEriksons/OneDrive - WorldHarbour\Desktop/Personal Review Files/Python Code/CSV Analysis/Transactions.csv', encoding ='unicode_escape')

#Dropping null value columns to avoid errors
df.dropna(inplace = True)

#Dropping first row of the dataset since it does not contain any value
df.drop(index = df.index[0], axis =0 , inplace = True)

#Get the list of all column names from headers
column_headers = list(df.columns.values)
print("The Column Header: ", column_headers)

#Using + operator to combine two columns
df["Period"] = df[["1Column", "2Column", "3Column", "4Column", "5Column", "6Column",]].apply("-".join, axis=1)

print(df["Period"])

#Investigate the error: ValueError: Cannot set a DataFrame with multiple columns to the single column Period

#Export as HTML file
#df.to_html('C:/Users/EriksEriksons/OneDrive - WorldHarbour\Desktop/Personal Review Files/Python Code/CSV Analysis/Transactions.html')

#To print first 5 rows use the code below
#print(df.head())

#To print the entire set use the code below
#print(df)



