from flask import Flask  # 載入 Flask
from flask import session
from flask import render_template  # 載入 render_template
from flask import request  # 載入 request 物件
# print("請求方法", request.method)
# print("通訊協定", request.scheme)
# print("主機名稱", request.host)
# print("路徑", request.path)
# print("完整網址", request.url)
# print("瀏覽器和作業系統", request.headers.get("user-agent"))
# print("語言偏好", request.headers.get("accept-language"))
# print("引薦網址", request.headers.get("referrer"))
from flask import redirect  # 載入 redirect 函式
import json as js


# 建立 Application 物件, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static",  # 靜態檔案的資料夾名稱
    static_url_path="/"  # 靜態檔案對應的網址路徑
)
app.secret_key = "this is a secret about boni"  # 設定 session 密鑰


# 所有在 static 資料夾底下的檔案,都對應到網址路徑 /檔案名稱
@app.route("/")  # 函式的裝飾 (Decorator): 以函式為基礎,提供附加的功能
def home():
    return render_template("boni.html", name="66")
    # return redirect("/boni.html")
    # lang=request.headers.get("accept-language")
    # if lang.startswith("en"):
    #     return redirect("/en/")
    # else:
    #     return redirect("/zh/")


@app.route("/66.html")
def dad():
    return render_template("66.html")


@app.route("/account", methods=["POST"])  # 限定接收資料的方法 POST OR GET 通常用於表單
def account():
    # recieve request with POST method
    # request.form["name in html"]
    # receive request with GET method
    # request.args.get("name in html", "value")
    account = request.form["account"]
    password = request.form["password"]
    member = request.form["member"]
    session["username"] = account[0:3]
    if(account == "lou8168168" and password == "lou10130244"):
        return render_template("boni.html", name=account)
    print(account, password, member)
    return render_template("boni.html", name="遊客")


@app.route("/hello")
def hello():
    return "hello "+session["username"]

# @app.route("/en/")
# def EnglishMode():
#     return js.dumps({
#             "status":"ok",
#             "text":"Hello Flask"
#         })
# @app.route("/zh/")
# def ChineseMode():
#     return js.dumps({
#         "status":"wrong",
#         "text":"你好"
#     },ensure_ascii=False) # 指示不要用 ASCII 編碼處理中文

# 練習傳遞函式參數
# @app.route("/user/<name>")
# def handleUser(name):
#     if name=="lou":
#         return "Hello master"
#     else:
#         return "Hello "+name

# 練習接收request參數
# @app.route("/getSum")
# def sum():
#     maxNum=request.args.get("max",100)
#     minNum=request.args.get("min",10)
#     result=0
#     for cnt in range(int(minNum),int(maxNum)+1):
#         result+=cnt
#     return str(result)


if __name__ == "__main__":  # 如果以主程式執行
    app.run(port=3000)  # 立刻啟動伺服器, 可透過 port 參數指定埠號
