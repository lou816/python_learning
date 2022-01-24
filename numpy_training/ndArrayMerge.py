import numpy as np

arr1=np.array([
    [1,2,3],
    [3,4,5]
])

arr2=np.array([
    [6,7,8],
    [8,9,10]
])

arr3=np.array([
    [5,10],
    [10,15]
])

result1=np.vstack((arr1,arr2))
result2=np.hstack((arr1,arr2,arr3))
print(result1)
print(result2)