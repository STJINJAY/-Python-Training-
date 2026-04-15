# 題目

# 1. 猜數字遊戲（Guess the Number)
# 產生一個 1~100 的隨機數字
# 讓使用者重複猜，提示「太大」、「太小」
# 猜對才結束，並顯示猜的次數

# 我的程式碼:
import random

answer=random.randint(1,101) # 這行會產生 1 到 101 之間的隨機數，包含 101

while answer<100: # 只要答案小於 100 就一直猜
    guess=int(input())
    if guess==answer:
        print("答對了")
        break
    elif guess<answer:
        print("太小")
    elif guess>answer:
        print("太大")

# 參考正確程式碼:
import random

answer = random.randint(1, 100)

while True: # 玩家能一直猜，直到猜對才結束
    guess = int(input("請猜一個 1~100 的數字："))
    if guess == answer:
        print("答對了！")
        break
    elif guess < answer:
        print("太小了！")
    else:
        print("太大了！")
