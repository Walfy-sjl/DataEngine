import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

data = {'Chinese': [66, 95, 93, 90,80,80],'English': [65, 85, 92, 88, 90,90],'Math': [np.NAN, 98, 96, 77, 90,90]}
df = pd.DataFrame(data,index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei', 'DianWei'])
print(df)

# 去除重复行
df = df.drop_duplicates()
# df['Math'] = df['Math'].fillna(60)
# df.Math = df.Math.astype(np.int64)

print(df)

def total_score(df):
    df['总分'] = df['Chinese'] + df['English'] + df['Math']
    return df


# 求成绩的和，用老师讲的 apply 方法
df = df.apply(total_score, axis=1)
# 或者可以用这个方法求和
# 按照总分排序，从高到低，此时有缺失值
df.sort_values(['总分'], ascending=[False], inplace=True)

print(df)

df['Math'].fillna(df['Math'].mean(), inplace=True)
print(df)