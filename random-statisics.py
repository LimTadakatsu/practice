#隨機模組
import random
#隨機選取
data=random.sample([1,5,6,10,20],3)#多個隨機選取
print(data)
data=random.choice([1,5,6,10,20])#隨機選取
print(data)
#隨機調換順序
data=[1,5,8,20]
random.shuffle(data)
print(data)
#隨機取得亂數
data=random.random()# 0~1之間的隨機亂數
print(data)
data=random.uniform(60,100)# 60~100之間的隨機亂數
print(data)
#常態分配亂數
#平均數100 ,標準差10 , 得到的資料多數在 90~110之間
data=random.normalvariate(100,10)
print(data)
#統計模組
import statistics as stat
data=stat.mean([1,4,5,8,11])#平均數
print(data)
data=stat.median([1,4,5,8,11])#中位數
print(data)
import statistics as stat
data=stat.stdev([1,4,5,8,11])#標準差
print(data)