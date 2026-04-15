# 題目
# 計算平均（函式 + *args + round()）
# 請定義一個函式 average(*scores)，回傳所有分數的平均值（四捨五入至小數點第一位）。

# 我的程式碼
def average(*scores):
    ave=sum(*scores)/len(*scores)
    return ave
scores=input("請輸入成績：")
scores_list=list(int(n)for n in scores.split())
print(average(scores_list))

# 修正程式碼
def average(*scores):
    if not scores:
        return "沒有成績可計算"
    ave = round(sum(scores) / len(scores), 1)
    return ave

scores = input("請輸入成績：")  # 例如輸入：90 80 100
scores_list = [int(n) for n in scores.split()]

print("平均分數為：", average(*scores_list))