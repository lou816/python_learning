# 網路爬蟲 關鍵心法: 盡可能讓程式像一個使用者的角度去跑
# 抓取 AJAX 類型網頁資料
# AJAX 網頁開啟流程
# 發送網址給 web_server -> web_server 回傳"不"含內容的 html -> 
# 第二次發送網址 -> web_server 回傳內容 html
# EX 抓取 medium.com 的 文章標題
import urllib.request as req
url = "https://medium.com/_/api/home-feed"
# 建立一個 Request 物件, 附加 Request Headers 的 資訊
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"

})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# 解析JSON原始碼, 取得每篇文章標題 

import json
data=data.replace("])}while(1);</x>","")
data = json.loads(data)

# 取得 JSON 資料中的文章標題
posts= data["payload"]["references"]["Post"]

for key in posts: 
    post = posts[key]
    print(post["title"])