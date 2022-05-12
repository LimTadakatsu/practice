# #參數的預設資料
# def power(base,exp=0): #base底數 exp次方數
#     print(base**exp)
# power(3,2)
# power(4)
# #使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,3)
# divide(n2=2,n1=4) #參數名稱對應
#無限參數資料
def avg(*ns): #avg平均
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)