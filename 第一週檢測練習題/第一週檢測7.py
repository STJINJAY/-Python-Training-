# 題目

# 7. 密碼驗證器
# 輸入密碼（例如 1234），最多只能錯三次，正確就登入

# 我的程式碼
import random
code=random.randint(1000,10000)
n=0
while n<3:
    enter=int(input())
    if code==enter:
        print("登入成功")
    else:
        n+=1
        print("請重新輸入")
if n==3:
    print("登入失敗")

# 修正程式碼
import random

code = random.randint(1000, 9999)  # 產生 1000~9999 的四位數密碼
n = 0

while n < 3:
    enter = int(input("請輸入四位數密碼："))
    if enter == code:
        print("登入成功")
        break
    else:
        n += 1
        if n < 3:
            print("請重新輸入")
        else:
            print("登入失敗")