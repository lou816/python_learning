import numpy as np

# 1-dim index
data=np.array([1,2,3,4])
print(data[0])
# n-dim index
data=np.array([
    [1,2],
    [2,3]
])
print(data[0,0])
# 1-dim 切片
data=np.array([1,2,3,4])
print(data[0:3]) # [1,2,3]
print(data[:2])  # [1,2]
# n-dim 切片
data=np.array([
    [[1,2],[2,3]],
    [[3,4],[4,5]],
    [[5,6],[6,7]]
])
print(data[1:2,:1,1:]) # [[[3]]]
print(data[...,1:])