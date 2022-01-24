# 網路爬蟲 關鍵心法: 盡可能讓程式像一個使用者的角度去跑
# IF 資料格式為 JSON 用 JSON 模組去抓
# IF 資料格式為 HTML 用 BeautifulSoup 第三方套件解析
# simple HTML format
# <html>
#   <head>
#       <title> HTML TITLE </title>
#   </head>
#   <body>
#       <div class = "list">
#           <span>階層結構</span>
#           <span>樹狀結構</span>
#       </div>
#   </body>
# </html>
#
# EX 抓取MOVIE PTT SOURCE HTML
#
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件, 附加 Request Headers 的 資訊
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# 解析原始碼, 取得每篇文章標題 
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title") # 尋找所有 class = "title" 的 div 標籤

for title in titles:
    if title.a != None:
        print(title.a.string)
