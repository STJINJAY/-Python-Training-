# 題目
# 尋找數字（for-else）
# 請寫一段程式碼，從列表中尋找使用者輸入的數字，如果找到則顯示「找到數字」，找不到則印出「找不到」。

# 使用 for-else 語法完成，列表內容為 [7, 14, 21, 28, 35]。

# 我的程式碼
numbers=[7,14,21,28,35]
n=int(input("請輸入要尋找數字："))
for x in range(0,5):
    if n==numbers[x]:
        print("找到數字")
        break
else:
    print("找不到")