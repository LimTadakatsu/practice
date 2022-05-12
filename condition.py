#判斷式
x=input("請輸入數字: ")
x=int(x) #轉換成數字
if x>100:
    print("大於100")
elif x==100:
    print("等於100")
else:
    print("小於100")
#四則運算
n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
op=input("請輸入:+,-,*,/:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("無法運作")