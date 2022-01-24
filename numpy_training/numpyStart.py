import numpy as np
# dim
#   1-dim
#       np.array([list])      列表建立陣列
#       np.empty(elementCnt)  建立值未指定陣列
#       np.zeros(elementCnt)  建立值都為0陣列
#       np.ones(elementCnt)   建立值都為1陣列
#       np.arange(elementCnt) 建立連續資料陣列 EX.arange(10) [0,1,2,3,4,5,6,7,8,9]
#   2-dim
#       np.array([
#           [row1]
#           [row2]
#           [row3]
#       ])
#       np.empty([row,col])
#       np.ones([row,col])
#       np.zeros([row,col])
#   n-dim 以此類推


data=np.array([3,4,5])
print(data)


