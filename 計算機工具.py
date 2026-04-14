import re history=[]
pattern=r"[0-9\.\+\-\*\/\(\)]+$"
while True:
formula=input("請輸入運算式(或是按q離開):")
if formula.lower()=="q":
  break
if re.match(pattern,formula):
  try:
    result=eval (formula)
    history.append (f"{formula}={result}")
    print (result)
  except:
    print("計算錯誤，請檢查輸入")
  else:
    print("輸入不合法，只能使用數字、運算符號（+-*/）、小數點和括號")
with open("history.txt", mode="a" ,encoding="utf-8") as file:
  for record in history:
    file.write(record+"\n")
  print("\n所有資料已存到history.txt")