# #point 實體物件的設計: 平面座標上的點
class point:
    def __init__(self):
        self.x=3
        self.y=4
#建立第一個實體物件
p1=point()
print(p1.x,p1.y)
#建立第二個實體物件
p2=point()
print(p2.x+1,p2.y+1)

#point 實體物件的設計: 平面座標上的點
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#建立第一個實體物件
p1=point(3,4)
print(p1.x,p1.y)

#建立第二個實體物件
p2=point(55,66)
print(p2.x+1,p2.y+1)
#FullName 實體物件的數計: 分開紀錄姓,名資料的全名
class Fullname:
    def __init__(self):
        self.first="C.W."
        self.last="Peng"
name1=Fullname()
print(name1.first,name1.last)

class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name2=Fullname("C.T","Peng")
print(name2.first,name2.last)
    