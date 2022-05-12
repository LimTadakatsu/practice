#定義函式 重複的函式重複呼叫
def multiply(n1,n2):
    print(n1*n2)#不一定需要print可以只印結果
    return n1*n2
# 呼叫函式
value=multiply(3,4)+multiply(10,5)
print(value)
# multiply(3,4)
# multiply(5,6)

#程式的包裝
def calculate(max):
    sum=0
    for x in range(1,max+1):
        sum=sum+x
    print(sum)

calculate(10)
calculate(565)