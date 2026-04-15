# 題目

# 4. 數字加總器
# 使用者輸入一個正整數 n，程式輸出 1+2+3+...+n 的總和

# 我的程式碼
n=int(input())
sum=0
for x in range(1,n+1):
    sum=sum+x
print(sum)

# 簡化程式碼
n = int(input())
print(sum(range(1, n + 1)))