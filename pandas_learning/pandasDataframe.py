import pandas as pd

# 建立資料
data=pd.DataFrame({
    "name":["leo","bob","boni"],
    "salary":[100,1000,10000]
}, index=["a","b","c"])
print(data,"\n")
# 觀察資料
# 大小      data.size 
# 列,攔     data.shape 
# 索引      data.index 

# 取得資料
# 取得rowN  data.iloc[n] == data.loc["index[n]"]
# 取得colN  data["key"]
names=data["name"]
print(names.str.upper(),"\n")
salaries=data["salary"]
print(salaries.mean())

# 新增欄位
# 直接給 data 新增一個 dictionary 或 建立一個 series(index要與原本的index相符) assign 給一個 dictionary
data["revenue"]=[1000,10000,100000]
data["rank"]=pd.Series([1000,10000,100000])
data["priority"]=pd.Series([1,2,3],index=["a","b","c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)