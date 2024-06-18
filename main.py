import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Печатаем исходный DataFrame
print("Исходный DataFrame:")
print(data.head())

# Создаем one hot encoding вручную
one_hot = pd.concat([data, pd.DataFrame({'robot': (data['whoAmI'] == 'robot').astype(int), 
                                         'human': (data['whoAmI'] == 'human').astype(int)})], axis=1)
one_hot = one_hot.drop('whoAmI', axis=1)

# Печатаем DataFrame с one hot encoding
print("\nDataFrame в one hot виде:")
print(one_hot.head())
