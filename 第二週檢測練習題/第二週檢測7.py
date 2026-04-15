# 題目
# 尋找最大值（使用 *args）
# 定義一個函式 find_max(*nums)，可以找出多個數字中的最大值。不得使用內建 max() 函式。

# 我的程式碼
def find_max(*nums):
    Max=nums[0]
    for n in nums[1:]:
        if n>Max:
            Max=n
    return Max
numbers=input("請輸入數字：")
number_list=list(int(n)for n in numbers.split())
print("最大值為：",find_max(*number_list))

# 正確程式碼
def find_max(*nums):
    if not nums:
        return "沒有數字可比"
    max_num = nums[0]
    for n in nums[1:]:
        if n > max_num:
            max_num = n
    return max_num

numbers = input("請輸入數字（用空格分隔）：")
if numbers.strip() == "":
    print("未輸入任何數字")
else:
    number_list = [int(n) for n in numbers.split()]
    print("最大值為：", find_max(*number_list))