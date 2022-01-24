# 網路連線
import urllib.request as net_request

# 取得網站source code(type: json, http, css)
src = "https://www.ntu.edu.tw/"
with net_request.urlopen(src) as response:
    data = response.read().decode("utf-8")
print(data)

# 串接、擷取公開資料
import urllib.request as net_request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with net_request.urlopen(src) as response:
    data = json.load(response)
# print(data)

# 取得公司名稱
clist = data["result"]["results"]
print(clist)
with open("company.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")