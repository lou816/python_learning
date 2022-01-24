# # 定義裝飾器
# def myDeco(cb):
#     def run():
#         print("123")
#         cb(100)
#     return run
# # 使用裝飾器
# @myDeco
# def test(n):
#     print("456",n)
# test()


# 定義 1+...+50 總和 func
def dec(cb):
    def calculate():
        tot = 0
        for n in range(51):
            tot += n
        cb(tot)
    return calculate


@dec
def add(v):
    print("結果是:", v)


@dec
def ENGadd(v):
    print("result is:", v)


add()
ENGadd()
