#定義生成器的函式
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 11
#呼叫並回傳生成器
gen=test() #建立生成器 yield都不會動 除非多了for迴圈
#搭配迴圈使用
for data in gen:
  print(data)

  def generateEven():
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number
    number+=2
evengenerator=generateEven()
for data in evengenerator:
    print(data)
print("=================")
#while迴圈使用
def generateEven():
    number=0
    while number<=1000:
      yield number
      number+=2
evengenerator=generateEven()
for data in evengenerator:
    print(data)
#另一種break寫法
def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
      yield number
      number+=2
evengenerator=generateEven(16)
for data in evengenerator:
    print(data)