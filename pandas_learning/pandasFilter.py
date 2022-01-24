from multiprocessing import Condition
import pandas as pd

# Series 的資料篩選
data=pd.Series([100,200,300])
dataStr=pd.Series(["abc","cde","efg"])
# 建立篩選條件
condition1=[True,False,True]
condition2=data>100
conditionStr=dataStr.str.contains("c")
# print(data[condition1])
# print(condition2)
# print(data[condition2])
# print(dataStr[conditionStr])

# DataFrame 的資料篩選
data=pd.DataFrame({
    "name":["abc","bcd","cde"],
    "len":[3,3,3]
})
# 建立篩選條件
condition=data["name"].str.contains("b")
# print(condition)
# print(data[condition])
# print(data)