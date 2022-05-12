def myFactory(base):
  def myDeco(callback):
    def run():
       print("裝飾器內",base)
       callback()
    return run
  return myDeco

@myFactory(3) #裝飾器工廠多了一個()可以多一個參數
def test():
  print("普通函式")

test()

print("======")

def myFactory(base):
  def myDeco(callback):
    def run():
       print("裝飾器內",base)
       result=base*2
       callback(result)
    return run
  return myDeco

@myFactory(3) #裝飾器工廠多了一個()可以多一個參數
def test(result):
  print("普通函式",result)

test()