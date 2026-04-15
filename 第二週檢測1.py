# 題目
# 倒數計時器（搭配 break）
# 請寫一個函式 countdown(n)，會從 n 倒數到 1，每秒顯示一次數字，如果數字為 3 就提前停止。

# 我的程式碼
import time
def countdown(n):
    while n>=1:
        print(n)
        n-=1
        time.sleep(1)
        if n<3:
            print("(提前結束)")
            break
n=int(input("請輸入倒數幾秒："))
countdown(n)

# 正確程式碼
import time

def countdown(n):
    while n >= 1:
        if n == 3:
            print("(提前結束)")
            break
        print(n)
        time.sleep(1)
        n -= 1

n = int(input("請輸入倒數幾秒："))
countdown(n)