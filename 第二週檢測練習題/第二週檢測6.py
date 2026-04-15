# 題目
# 問候系統（函式參數名稱對應）
# 請寫一個函式 welcome(time, name)，輸出「早安／午安／晚安，xxx！」
# 使用者可以用參數名稱指定順序

# 我的程式碼
def welcome(time,name):
    print(f"{time}，{name}!")
name=input("請輸入名字：")
time=input("請輸入時間：")
welcome(time,name)