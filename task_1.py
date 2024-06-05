from pandas import DataFrame, get_dummies
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = DataFrame({'whoAmI': lst})
# print(data)

# print(get_dummies(data['whoAmI']))

data.loc[data['whoAmI'] == 'human', 'human'] = True  # 1
data.loc[data['whoAmI'] == 'robot', 'human'] = False  # 0
data.loc[data['whoAmI'] == 'human', 'robot'] = False  # 0
data.loc[data['whoAmI'] == 'robot', 'robot'] = True  # 1

# data.pop('whoAmI')
# print(data)
print(data[['human', 'robot']])
