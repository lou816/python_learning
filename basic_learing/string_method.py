string = "   abc def   "

print(string.rstrip())  # 去除右空格
print(string.lstrip())  # 去除左空格
print(string.upper())  # 轉大寫
print(string.lower())  # 轉小寫
print(string.title())  # 首個單字轉大寫
print(string.find("a"))  # 找到特定字元/串index
print(string.replace("a", "c"))  # 改變全部特定字串
print("abc" in string)
print("abc" not in string)
