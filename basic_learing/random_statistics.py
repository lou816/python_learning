# 隨機模組
import random
# 隨機選取 choice 隨機選取一個 sample 隨機選取n個
data = random.choice([1,5,6,10,20])
print(data)
data = random.sample([1,5,6,10,20],3)
print(data)

# 隨機調換順序
data = [1,5,6,10,20]
random.shuffle(data)
print(data)

# 隨機取得0-1之間亂數 uniform可自訂區間
data = random.random()
print(data)
data = random.uniform(0.0, 1.0)
print(data)

# 取得常態分配亂數 取得資料會落在平均數的標準差範圍內
data = random.normalvariate(100,10)
print("常態分配", data)

# 統計模組
import statistics as stat

# 平均數
result = stat.mean([1,5,6,10,20])
print(result)

# 中位數
result = stat.median([1,5,6,10,20,1000])
print(result)

# 標準差
result = stat.stdev([1,5,6,10,20,1000])
print(result)