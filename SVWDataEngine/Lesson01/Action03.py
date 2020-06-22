'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''

import numpy as np
import pandas as pd

# 原始数据
df = pd.read_csv(r"car_complain.csv", encoding='utf-8')
# 拆分problem字段
res = df.drop('problem', 1).join(df['problem'].str.get_dummies(','))
# print(res.head())
# tags = res.columns[8:]

problem_bybrand_counts = res.groupby(['brand'])['id'].agg(['count'])
print(problem_bybrand_counts.reset_index(drop=False))
df11 = problem_bybrand_counts.reset_index(drop=False)
# problem_bybrand_counts2 = res.groupby(['brand'])['car_model'].transform(lambda x: len(x.unique()))
# print(problem_bybrand_counts2)
problem_bybrand_counts3 = res.pivot_table(index='brand', values='car_model', aggfunc=pd.Series.nunique)
print(problem_bybrand_counts3.reset_index(drop=False))
df22 = problem_bybrand_counts3.reset_index(drop=False)
df33 = pd.merge(df11, df22, on='brand')
df33['times'] = round(df33['count'] / df33['car_model'], 1)
# print(df33.info())
print(df33)
# problem_bymodel_counts = res.groupby(['car_model'])['id'].agg(['count'])
# print(problem_bymodel_counts)
# problem_bybrandmodel_counts = res.groupby(['brand','car_model'])['id'].agg(['count'])
# print(problem_bybrandmodel_counts)

# dataset = res.set_index(['id','brand','car_model','type','desc','datetime','status']).stack().reset_index(drop=False)
# dataset.rename(columns={"level_7":"Question",'0':'value'},inplace=True)
# print(dataset)

# datasetfilter=dataset.drop(dataset[dataset['Question'] == 0].index)   # axis默认等于0，即按行删除，这里表示按行删除第0行
# print(datasetfilter)
