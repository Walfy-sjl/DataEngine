import numpy as np
import pandas as pd

a= pd.Series([1,1,2,3,4,5])
print(a)

a= pd.Series([1,1,2,3,4,5],index=['a','d','c','b','e','f'],dtype=float)
print(a)

dic = {"name":'zhangsan','age':33,'sex':'man'}
a = pd.Series(dic)
print(a)

a = pd.Series(dic,index=['name','color'])
print(a)

a = pd.DataFrame(a,columns=['clo1'])
print(a)

a = pd.DataFrame({'coll':dic})
print(a)