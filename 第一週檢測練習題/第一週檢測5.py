# 題目

# 5. 乘法表選單
# 使用者輸入一個數字，例如 7，就列出 7 x 1 ~ 9 的乘法表

# 我的程式碼
n=int(input())
for x in range(1,10):
    print(f"{n}*{x}={n*x:2}")

# 進階程式碼:多張乘法表（輸入開始與結束數）
start = int(input("起始數字："))
end = int(input("結束數字："))

for n in range(start, end + 1):
    for x in range(1, 10):
        print(f"{n}*{x}={n*x:2}")
    print()