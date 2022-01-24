# 有順序可改列表 List == array
Int_List = [1, 2, 3]
String_List = ["a", "b", "c"]
# 更改 List 中的值
Int_List[-1] = 5
print("current /int list: ")
print(Int_List)
Int_List[2] = 4
String_List[0] = "abc"
print("current /int list: ")
print(Int_List)
print("current string list: ")
print(String_List)
# 取得資料 [start:end] 包前不包後
print(Int_List[1:2])
# 插入
Int_List += [5, 6, 7]
String_List += ["d", "e", "f"]
print("current /int list:")
print(Int_List)
print("current string list:")
print(String_List)
# 取得長度
length = len(String_List)
print(length)
# 巢狀List == 2dimensional array
Student_Table = [["Alice", "Leo", "Emily"], [
    "109001", "109002", "109003"], ["Taipei", "Taichung", "Kayi"]]
# 有順序不可改列表 Tuple == constant list
Int_Tuple = (3, 4, 5)
String_Tuple = ("a", "b", "c")


# duplicates item list
zeros = [0] * 100
print(zeros)

# list plus list
combin = Int_List + String_List
print(combin)


# list function used to create list with iterable things  ex. range,string....
# list[1,2,3.....n]
num = list(range(20))
print(num)

# list[string]
chars = list("hello")
print(chars)

# reverse list
reverse_num = num[::-1]
print(reverse_num)

# unpacking list
num = [4, 5, 6]
a, b, c = num
# packing list
num = list(range(100))
a, b, *queue = num
print(f"{a}, {b}\n{queue}")
