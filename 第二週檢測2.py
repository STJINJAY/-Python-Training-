# 題目
# 購物計算
# 定義一個函式，能計算所有商品的總價，並加上運費。

# 範例輸入：
# 100, 200, 50
# 100, 200, 50, shipping=0

# 範例輸出：
# 410
# 350

# 我的程式碼
def total_price(*all_price,shipping=60):
    p=0
    for n in all_price:
        p+=n
    total=p+shipping
    return total
enter_price=input("請輸入所有商品價格：")
price_list=[int(n) for n in enter_price.split()]
print("總共",total_price(*price_list),"元")