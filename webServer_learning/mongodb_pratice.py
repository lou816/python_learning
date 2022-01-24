# 載入 pymongo 套件
import pymongo

# 連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient(
    "mongodb+srv://account:password@mrdotcluster.r178b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.MEMBER  # 選擇要操作 test 資料庫
collection = db.account  # 選擇操作 users 集合

# 新增資料
# 集合.insert_one({data}) 插一筆
# 集合.insert_many({data1...dataN}) 插很多筆

# 實際操作
# collection.insert_one({
#     "name":"YY",
#     "account":"a0966026053",
#     "password":"a0938951531"
# })


# 查詢資料
# 集合.find/find_one(ObjectId(objID)/{查詢條件
#   條件都必須成立用"$and":[{條件1},{條件2}...]
#   條件擇一成立用"$or":[{條件1},{條件2}...]
#   },sort=[(排序方式
#       "排序參數",
#           升序用pymongo.ASCENDING
#           降序用pymongo.DESCENDING
#   ]) 回傳 doc
# 集合.find() 回傳全部 doc
# for cnt in 全部 doc 來印出全部資料

# 實際操作
# from bson.objectid import ObjectId
# data=collection.find_one(ObjectId("61e79f4b28001ada5e484afe"))
# data=collection.find_one({
#     "$and":[
#         {"name":"boni"},
#         {"account":"boni0312"}
#     ]
# })
# data=collection.find({
#         "$or":[
#             {"name":"boni"},
#             {"name":"YY"}
#         ]
#     },sort=[("name",pymongo.ASCENDING)])
# for cnt in data:
#     print(cnt)
# print(data)
# print("特定資料總資訊",data)
# print("此資料帳號",data["account"])
# print("此資料密碼",data["password"])


# 更新資料
# 集合.update_one/update_many({篩選條件},{更新資訊})
#   前面的dictionary為條件,
#   後面的dictionary為
#       更新內容用"$set":{}
#       增加數字資料用"$inc":{}
#       數字乘倍數資料用"$mul":{}
#       清除欄位用"$unset":{}
# 接收集合.update_one/update_many回傳值.matced_count符合條件文件數量
# 接收集合.update_one/update_many回傳值.modified_count更新文件數量

# 實際操作
# result=collection.update_one/update_many({
#     "name":"boni"
# },{
#     # "$set":{
#     #     "name":"boni",
#     #     "account":"boni0312",
#     #     "password":"boni0312",
#     #     "age":8 # 本來沒此欄位,會新增此欄位
#     # }
#     # "$unset":{
#     #     "age":100 # 撤掉 age 欄位
#     # }
#     # "$inc":{
#     #     "age":2 # 會把 age 欄位值 +2 ,前提此欄位為int
#     # }
#     "$mul":{
#         "age":2 # 會把 age 欄位值 *2 ,前提此欄位為int
#     }
# })
# print("符合篩選條件數量",result.matched_count)
# print("實際更新資料數量",result.modified_count)


# 刪除資料
# 集合.delete_one/delete_many({刪除條件})

# 實際操作
# result=collection.delete_one/delete_many({
#     "name":"boni"
# })
# print("符合刪除條件數量",result.delete_count)

collect = collection.find()
print("當前資料")
for entity in collect:
    print(entity)

collect = collection.find()
print("更新後資料")
for entity in collect:
    print(entity)
