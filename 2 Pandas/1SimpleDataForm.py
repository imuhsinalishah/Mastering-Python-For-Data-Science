import pandas as pd
data = {
    'Name': ['Adil', 'Bakr', 'Chalie', 'David', 'Ebrahim'],
    'Age': [10, 20, 30, 40, 50],
    'Gender': ['M', 'F', 'M', 'F', 'M'],
    'city': ['nowsher', 'Bannu', 'Chad', 'Delhi', 'Espain']
}
df = pd.DataFrame(data)
print(df)


#  Example 2

data = [
    ['david',28,'M','Nowhera'],
    ['Bakr',20,'f','Bannu'],
    ['Chalie',30,'M','Chad'],
    ['Ebrahim',40,'M','Espain'],
    ['Adil',50,'F','Delhi'],
]

dfs = pd.DataFrame(data,columns=['Name','Age','Gender','City'])
print(dfs)