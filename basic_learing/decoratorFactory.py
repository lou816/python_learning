# def myFactory(base):
#     def myDeco1(cb):
#         def run():
#             print("裝飾器內的程式",base)
#             result=base*3
#             cb(result)
#         return run
#     return myDeco1
# @myFactory(4)
# def test(result):
#     print("普通函式",result)

# test()

# 計算 1+...+50
def decFactory(max):
    def dec(cb):
        def calculate():
            tot=0
            for n in range(max+1):
                tot+=n
            cb(tot)
        return calculate
    return dec
@decFactory(100)
def show(v):
    print("結果是:",v)

@decFactory(10)
def showEng(v):
    print("result is:",v)
show()
showEng()