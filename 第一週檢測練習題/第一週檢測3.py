# 題目

# 3. 判斷是否為質數
# 輸入一個正整數，判斷它是否為質數（只能被 1 和自己整除）

# 我的程式碼
n=int(input())
for x in range(1,n+1):
    for y in range(2,n):
        key=x%y
if x%y==0:
    print("否")
elif x%y!=0:
    print("是")

# 參考正確程式碼
n=int(input())

is_prime=True # 假設n是質數

if n<2:
    is_prime=False
else:
    for x in range(2,n):
        if n%x==0:
            is_prime=False
            break # 整除代表不是質數，所以跳出迴圈

if is_prime:
    print("是")
else:
    print("否")