import pandas as pd
data = {
    'Name': ['Adil', 'Bakr', 'Chalie', 'David', 'Ebrahim'],
    'Age': [10, 20, 30, 40, 50],
    'Gender': ['M', 'F', 'M', 'F', 'M'],
    'city': ['nowsher', 'Bannu', 'Chad', 'Delhi', 'Espain']
}
df = pd.DataFrame(data)
age_column = df['Age']
print ('select age column')
print (age_column)

name_city = df[['Name','city']]
print ('select name and city column')
print (name_city)
