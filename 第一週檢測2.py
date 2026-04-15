# 題目

# 2. 九九乘法表顯示
# 顯示 1~9的乘法表
# 格式整齊輸出，例如 3 x 4 = 12

# 我的程式碼:
for x in range(1,10):
    for y in range(1,10):
        print(x,"*",y,"=",f"{x*y}",end=" ")
    print()

# 參考正確程式碼;
for x in range(1,10):
    for y in range(1,10):
        print(f"{x}*{y}={x*y:2}",end=" ") # 格式化對齊	f"{變數:寬度}"，換行印東西	print(..., end=" ")
    print() # 換行	print()（不帶內容會換行）