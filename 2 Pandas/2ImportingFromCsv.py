import pandas as pd                  #import pandas
df = pd.read_csv('data.csv')         #import data
print("imported data from csv")      #print imported data
print(df.head())                     #first 5 rows


df.to_csv('data2.csv')                #save data
print("\n saved data to csv")         # print saved data

# to expoert data to excel
df.to_excel('data2.xlsx',sheet_name='sheet1')
print("\n saved data to excel")
print(df.head())
