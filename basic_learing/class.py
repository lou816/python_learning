# 定義類別、與類別屬性(封裝在類別中的變數和函式)
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:    
            print("Read from", src)

# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("dasd")

# 建立類別的實體物件
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(3,4)
print(p1.x, p1.y)
class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first+last
name1 = Name("C.W.", "Peng")
print(name1.fullname)

# 實體物件函式運用: Point 平面座標上的點
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # 定義實體函式
    def show(self):
        print(self.x,self.y)
    def distance(self, target) -> float:
        return ((target.x-self.x)**2 + (target.y-self.y)**2) ** 0.5
point1 = Point()
point2 = Point(3,4)
point1.show()
print("distance is ", point1.distance(point2))

# 實體物件設計: 包裝檔讀取程式
class File:
    def __init__(self, name) -> None:
        self.name = name
        self.file = None #尚無檔案 None==NULL
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8") 
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1 = File("data.txt")
f1.open()
data = f1.read()
print(data)
# 讀取第二個檔案
f2 = File("company.txt")
f2.open()
data = f2.read()
print(data)