import pandas as pd

df = pd.read_csv('data\FoodPrice_in_Turkey.csv')
# tg = df.iloc[3]

# tg = df.iloc[3:8]

# tg = df.iloc[:,4]

# tg = df.iloc[:,3:8]

# tg = df.iloc[3,7]

# tg = df.iloc[3:5,5:7]

# tg = df.loc[df.Year >= 2019]

# df.replace(5,10,inplace = True)

df.replace(52,'RR',inplace=True)
print(df.head())


