# 題目
# 判斷質數（使用 for + else）
# 請定義一個函式 is_prime(n)，
# 判斷 n 是否為質數，並印出「是質數」或「不是質數」，使用 for-else 完成，不可使用 break。

# 我的程式碼
def is_prime(n):
    if n<2:
        print("不是質數")
    elif n==2:
        print("是質數")
    else:
        for x in range(2,n):
            is_prime=True
            if n%x==0:
                is_prime=False
        if is_prime:
            print("是質數")
        else:
            print("不是質數")
n=int(input("請輸入一個數字："))
is_prime(n)

# 正確程式碼
def is_prime(n):
    if n <= 1:
        print("不是質數")
        return
    for i in range(2, n):
        if n % i == 0:
            print("不是質數")
            return
    else:
        print("是質數")
n=int(input("請輸入一個數字："))
is_prime(n)
