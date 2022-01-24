# 載入模組 
# import 模組名稱 as 別名
# 使用模組內建函式 
# 別名or模組名稱.內建函式名稱
# Example
import sys as system
system.path.append("modules")
print(system.platform)
print(system.maxsize)
print(system.path)
import geometry 
result = geometry.distance(1,1,5,5)
print(result)