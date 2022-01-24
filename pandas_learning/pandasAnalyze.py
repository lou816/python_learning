import pandas as pd

# 讀取資料
data=pd.read_csv("googleplaystore.csv") #讀入csv轉成DataFrame
# print(data)
# print("資料數量",data.shape)
# print("資料欄位",data.columns)
# print("評分平均數",data["Rating"].mean())
# # 找前100評分平均值發現平均值高於上限值
# print("前100APP評分平均數",data["Rating"].nlargest(100).mean())
# condition=data["Rating"]>5
# print(data[condition])
# rowIndex 10472 rating is bigger than 5

# 分析資料 : 安裝數量的各種統計數據
# print("平均數", data["Installs"].mean())
# print(data["Installs"])
# 透過上述兩行發現 Installs 為數字的字串
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+Free]",""))
# print(data["Installs"])
# print(data.iloc[10473])

# 基本資料的應用 : 關鍵字搜尋 
keyword=input("請輸入關鍵字: ")
condition=data["App"].str.contains(keyword, case=False)
print(data[condition]["App"])