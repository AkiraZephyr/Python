import pandas as pd
#s = pd.Series([10, 20, 30, 40])
#print(s)
#data = { 'Name': ['XXX', 'YYY', 'ZZZ'],
#        'Age': [25, 30, 35]}
#df = pd.DataFrame(data)
#print(df)

#data = [10, 20, 30, 40]
#s=pd.Series(data)
#print(s)
#s = pd.Series(data, index=['a', 'b', 'c', 'd'])
#print(s)
#data = {'a' : 100, 'b' : 200, 'c' : 300}
#s = pd.Series(data)
#print(s)
#print(s['b'])
#print(s[1])
#print(s[1:3])
#print(s+10)
#print(s*2)
#print(s[s > 100])
#print(s.index)
#print(s.values)
#print(s.dtype)
#print(s.head())
#print(s.tail())

#s = pd.Series([100,200,300],index=['a','b','c'])
#print(s['a'])
#data = {'Name': ['Alice', 'Bob', 'Charlie'],
#        'Age': [25, 30, 35]}
#df = pd.DataFrame(data,
#                  index = ['id1', 'id2', 'id3'])
#print(df['Name'])
#print(df[['Name', 'Age']])
#print(df.iloc[0])
#print(df.iloc[1:3])
#print(df.loc['id2'])
#print(df.loc[['id1', 'id3']])
#print(df[df['Age']>25])
#print(df[(df['Age'] > 25) & (df['Name'] == 'Charlie')])

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Original Series:\n", s)
s2 = s.reindex(['a', 'b', 'c', 'd'])
print("\nReindexed Series:\n", s2)
s2 = s.reindex(['a', 'b', 'c', 'd'], method='ffill')
s3 = s.reindex(['a', 'b', 'c', 'd'], method='bfill')
print(s2)
print(s3)