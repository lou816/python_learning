# 建立資料庫連線
import pymongo
client=pymongo.MongoClientclient = pymongo.MongoClient("mongodb+srv://lou8168168:lou10130244@mrdotcluster.r178b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Member_System

# 載入FLASK所需基本函式庫
from flask import * 
# 建立 Application 物件, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址路徑
) # 效果為跟目錄底下網址的資料會去public資料夾內尋找 

app.secret_key="this is a secret about boni" # 設定 session 密鑰


@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/member")
def mem():
    if "nickname" in session:
        return render_template("member.html",name=session["nickname"])
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤,請聯繫客服!!")
    return render_template("error.html",msg=message)

@app.route("/signup", methods=["POST"])
def signup():
    collection=db.account
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    print(nickname,email,password)
    result=collection.find_one({"nickname":nickname})
    if result != None:
        return redirect("/error?msg=信箱已被註冊")
    else:
        collection.insert_one({
            "nickname":nickname,
            "email":email,
            "password":password
        })
        return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    userdb=db.account
    email=request.form["email"]
    password=request.form["password"]
    result=userdb.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result == None:
        return redirect("/error?msg=帳號或密碼錯誤")
    session["nickname"]=result["nickname"]
    return redirect("/member")

@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

app.run(port=3000)