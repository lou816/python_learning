import numpy as np

data1=np.array([1,2,3])
data2=np.array([4,5,6])
# 基本運算
# data1+data2
# data1*data2
# data1/data2
# data>data2
# data1<data2
# data1==data
# 2-dim
data1=np.array([
    [1,2]
])
data2=np.array([
    [2,3,4],
    [3,4,5]
])
# data1.dot(data2) == data1@data2   內積
# np.outer(data1,data2)             外積
# 統計運算

data=np.array([
    [1,2,3],
    [4,5,6]
])
# data.sum(axis=維度)            和
# data.max(axis=維度)            最大值
# data.mean(axis=維度)           平均值
# data.std(axis=維度)            標準差
# data.cumsum(axis=維度)         所有element逐一相加