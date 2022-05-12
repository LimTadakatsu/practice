#計算1+2+3+...+50的裝飾器

def caclulate(callback):
  def run():
    total=0
    for n in range(51):
      total+=n
    callback(total)
  return run

@caclulate #裝飾器工廠多了一個()可以多一個參數
def show(result):
  print("結果是",result)

@caclulate
def showenglish(result):
  print("result is",result)


show()
showenglish()
print("======")
#計算1+2+3+...+n的裝飾器
#計算1+2+3+...+50的裝飾器
def caclulateFactory(max):
  def caclulate(callback):
    def run():
      total=0
      for n in range(max+1):
        total+=n
      callback(total)
    return run
  return caclulate

@caclulateFactory(100) #
def show(result):
  print("結果是",result)

@caclulateFactory(10)
def showenglish(result):
  print("result is",result)


show()
showenglish()
