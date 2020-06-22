import numpy as np
import pandas as pd

print("hello world!")

# df = pd.read_csv("salesdata.csv",encoding="ANSI",dtype={'month':np.str})
# df = pd.read_csv("E:\PythonCode\python\data0522\salesdata.csv", encoding="ANSI", dtype={'month': np.str})
df = pd.read_csv("salesdata.csv", encoding="ANSI", dtype={'month': np.str})
df.info()

dfym = df[(df['year'] > 2018) & (df['WRstatus'] == 'R/R')]
# dfym['month'] = dfym['month'].astype(int)

table = pd.pivot_table(dfym, values='sales', index=['year'], columns=['month'], aggfunc=[np.sum], fill_value='')
# filepath = r'C:\Users\LFY\Desktop\SalesData\asd.xlsx'
# writer = pd.ExcelWriter(filepath)
table


