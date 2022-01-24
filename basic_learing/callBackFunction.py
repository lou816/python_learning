# def test(arg):
#     arg(100) # 呼叫回乎函式,代入參數

# # 定義一個回呼函式
# def handle(data):
#     print(data)

# test(handle)

# def add(n1, n2, cb):
#     cb(n1+n2)

# def prt(result):
#     print("結果是:",result)

# add(3, 4, prt)

def calculator(n1, n2, cb):
    prt(cb(n1, n2))
def prt(v):
    print("答案是:",v)
def add(n1, n2):
    return n1+n2
def mul(n1, n2):
    return n1*n2

calculator(3,4,add)