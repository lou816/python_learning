import pandas as pd

data=pd.Series([11,22,33,44,55], index=["a","b","c","d","e"])
# 資料索引
# 觀察資料
print("資料型態",data.dtype)
print("資料數量",data.size)
print("資料索引",data.index)
# 取得資料: 
#   根據順序 data[0]
#   根據索引 data["a"]
# 數字運算: 基本、統計、順序
#   最大值  data.max()
#   總和    data.sum()
#   標準差  data.std()
#   中位數  data.median()
#   最大3   data.nlargest(3)
#   最小3   data.nsmallest(3)


data = pd.Series(["abc","cde","def"])
# 字串運算: 基本、串接、搜尋、取代
# 轉小寫    data.str.lower() 
# 字串長度  data.str.len()
# 連接字串  data.str.cat(sep="seperator")
# 取代      data.str.replace("source","target")
# 尋找      data.str.contains("target")