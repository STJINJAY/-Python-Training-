# 題目
# 自我介紹
# 定義一個函式 introduce(**info)，預設輸出 "未知" 的資訊欄位，如果有提供 name、age、hobby 就顯示：

# 輸出：
# 名字：小花
# 年齡：未知
# 興趣：跳舞

# 我的程式碼
def introduce(**info):
    for key,value in introduce:
        print(f"{key}：{value}")
introduce(name="阿杰",age="18",hobby="打排球")

# 正確程式碼
def introduce(**info):
    name = info.get("name", "未知")
    age = info.get("age", "未知")
    hobby = info.get("hobby", "未知")

    print(f"名字：{name}")
    print(f"年齡：{age}")
    print(f"興趣：{hobby}")