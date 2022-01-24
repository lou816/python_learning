import numpy as np

data=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [2,4,6,8]
])
rows=np.vsplit(data,3)
cols=np.hsplit(data,4)
for row in rows:
    print(row)
# [[1,2,3,4]]
# [[5,6,7,8]]
# [[2,4,6,8]]
for col in cols:
    print(col)
