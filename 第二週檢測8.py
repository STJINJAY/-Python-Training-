# 題目
# 密碼三次機會（while + break + else）
# 請寫一段程式，
# 讓使用者最多輸入三次密碼 "1234"，若輸入正確顯示「登入成功」，否則三次錯誤就輸出「登入失敗」。

# 我的程式碼
password="1234"
n=0
while n<3:
    enter=input("請輸入密碼：")
    if enter==password:
        print("登入成功")
        break
    else:
        print("密碼錯誤")
        n+=1
if n==3:
    print("登入失敗")

# 優化程式碼
password = "1234"
n = 0
while n < 3:
    enter = input("請輸入密碼：")
    if enter == password:
        print("登入成功")
        break
    else:
        print("密碼錯誤")
        n += 1
else:
    print("登入失敗") 