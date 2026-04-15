# 題目

# 8. 數字統計遊戲（統計偶數個數)
# 使用者輸入 n 個數字，統計其中偶數的個數

# 我的程式碼
input(number=[])
x=0
for n in range[]:
    if n%2==0:
        x+=1
print("有",x,"個偶數")

# 修正程式碼
s = input("請輸入一串整數，用空白分開：")
number = list(map(int, s.split()))  # 把字串分割並轉成整數清單

x = 0
for n in number:
    if n % 2 == 0:
        x += 1

print("有", x, "個偶數")