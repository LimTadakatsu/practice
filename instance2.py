#point 實體物件的設計 : 平面座標上的點
class point:
    def __init__(self,x,y,):
        self.x=x
        self.y=y
    #定義實體方法
    def show(self):
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return(((self.x-targetx)**2)+(self.y-targety)**2)**0.5
p=point(3,4)
p.show() #呼叫實體方法/函式
result=p.distance(0,0) #計算座標3,4 和座標0,0之間的距離
print(result)

#file 實體物件的設計 : 包裝檔案讀取的程式
class file:
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟檔案:初期是None (N要大寫)
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=file("data.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=file("data.txt")
f2.open()
data=f2.read()
print(data)