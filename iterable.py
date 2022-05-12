#可疊代資料
#字串，列表，集合，字典

#for 迴圈
#for 變數名稱 in 可疊代的資料: {}集合是沒有順序性的
for x in [3,5,2,"ㄚㄚㄚㄚ"]:
    print(x)
dic= {"a":3,"b":4}
for x in dic:
    print(x)
    print(dic[x])

#內建函式
#max(可疊代資料)

result=max([10,2,30,1])
print(result)
result=max("xaz")
print(result)
result=max({10,200,30,50})
print(result)

#sorted
result=sorted("cba")
print(result)
result=sorted({"-85,-87,22,87485645"})
print(result)