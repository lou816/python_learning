# 連續爬蟲
# 網路爬蟲 關鍵心法: 盡可能讓程式像一個使用者的角度去跑
# EX 抓取八卦 PTT SOURCE HTML
#
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件, 附加 Request Headers 的 資訊
    request = req.Request(url, headers = {
        "cookie":"over18=1",
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
    # 抓取上一頁的url
    nextLink = root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]
# 抓取一個頁面的標題
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc"+getData(url)
for i in range(0,3):
    url = "https://www.ptt.cc"+getData(url)
    # print(url)
    i+=1
