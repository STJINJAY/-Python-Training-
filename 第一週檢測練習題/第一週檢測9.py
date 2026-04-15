# 題目

# 9. 倒數計時器
# 輸入一個數字，從該數字倒數到 0，每秒顯示一個數字

# 我的程式碼
import time
n=int(input())
for x in range(n,-1,-1):
    print(x)
    time.sleep(1)
    if x==0:
        break
print("時間到")

#正確程式碼
import time

n = int(input("請輸入倒數秒數："))

for x in range(n, -1, -1):  # 從 n 到 0（含 0）
    print(x)
    time.sleep(1)

print("時間到！")