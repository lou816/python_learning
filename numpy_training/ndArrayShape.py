import numpy as np

data=np.array([1,2,3]).reshape(3,1)
dataT=data.T
print(data.shape)
print(dataT.shape)
data3d=np.array([
    [[1,1,1],[2,2,2],[3,3,3]],
    [[2,2,2],[3,3,3],[4,4,4]],
    [[3,3,3],[4,4,4],[5,5,5]]
])  # (3,3,3)
dataNew=data3d.ravel()
print(dataNew)
dataNew=dataNew.reshape(9,3)
print(dataNew)