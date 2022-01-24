# 定義建立生成器函式
# def test():
#     yield 3
#     yield 5
# 呼叫並回傳生成器
# gen=test()
# print(gen)
# 搭配 for 迴圈中使用
# for d in gen:
#     print(d)

def generatorEven():
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number

evenGenerator=generatorEven()
for data in evenGenerator:
    print(data)