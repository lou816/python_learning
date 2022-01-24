# pandas 為資料分析模組
# 主要用於建立 1-dim 的 Series 和 2-dim 的 DataFrame 以及資料操作

import pandas as pd

data=pd.Series([20,10,15])
# 以下操作都可以插入print(data)來看結果
# print("Max", data.max()) 最大值
# print("Median", data.median()) 中位數
# data=data*2 data裡面的值*2
# data=data==20 data裡面的值跟20做比較assign一個bool table給data

data=pd.DataFrame({
    "name":["Leo","John","Bob"],
    "salary":[3000,30000,300000]
})
# 以下操作都可以print來看結果
# data["name"] 印出特定欄位
# data.iloc[row_number] 取出特定 row 資料