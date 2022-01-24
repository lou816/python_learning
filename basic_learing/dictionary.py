# 集合的運算 in 在集合內 not in 不在集合內 & 交集 | 聯集 -差集 ^反交集 set(字串) 把字串拆解成元素
set1 = {1,2,3}
set2 = {2,3,4}
print(3 in set1)
print(5 not in set1)
Intersection = set1&set2
print(Intersection)
Union = set1|set2
print(Union)
Difference = set1-set2
print(Difference)
Anti_intersection = set1^set2
print(Anti_intersection)
s = set("ABCA") 
print(s)
# 字典的運算 key:value 比對 in 是比對key del 刪除
dic = {"1":"a","2":"b","3":"c"}
dic["1"] = "d"
print(dic["1"])
print("1" in dic)
del dic["1"]
# List-Dictionary translation
trans = {x:x*2 for x in [3,4,5]}
print(trans)
