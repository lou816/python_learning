# 建立檔案並且打開
# file = open("data.txt", mode="w", encoding="utf-8")
# file.write("hello")
# file.close()
#=======================================================

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")

# 讀取檔案
# file.read() 讀取全部
# 用for line in file 做一行一行讀取
sum = 0
with open("data.txt", mode="r", encoding="utf-8") as file:
    # data = file.read()
    for line in file:
        sum += int(line)
# print(data)
print(sum)

# 讀取、寫入 json 檔案
import json
with open("config.json", mode="r") as file:
    data = json.load(file)
print("name: ", data["name"])
print("version: ", data["version"])
data["new name"] = data["name"]
data["new version"] = data["version"]
with open("config.json", mode="w") as file:
    json.dump(data, file)