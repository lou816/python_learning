# 定義函式 
# def 函式名稱(參數名稱 = 預設資料、也可用指標接收不固定個數的參數): 
#     運算內容
#     return 回傳值
def multipleier(input1 = 100, input2 = 100):
    print("input1 is ", input1)
    print("input2 is ", input2)

    return input1*input2
def calculate(index):
    sum = 0
    for n in range(1,index):
        sum += n
    print(sum)
def say(*msgs):
    for msg in msgs:
        print(msg)
# 呼叫函式 呼叫時如果有assign值給特定參數名稱不用注意前後順序
print(multipleier(3,4))
print(multipleier())
print(multipleier(input2=1,input1=20))
say("abc","shdis","jsiajfi")
calculate(100)