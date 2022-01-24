# while loop else 迴圈結束前會做的事
n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
else:
    print(sum)
# for loop range(start,end)包前不包後
sum = 0
for x in "hello":
    print(x)
for x in range(3, 6):
    print(x)
for y in range(1, 11):
    print(y)
    sum += y
    if y == 5:
        break
    else:
        continue
# 此else是當for loop complete 後執行的
else:
    print(sum)
print(sum)


# 找出平方根
# input 9 ouput 3
num = input("輸入一個數字\n")
num = int(num)
for x in range(num):
    if x**2 == num:
        print("平方根為", x)
        break
else:
    print("此值沒有平方根")
