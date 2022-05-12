#回呼函式
def test(arg):
  arg()

def handle():
    print(100)

test(handle) #利用上面印出下面
#arg裡面裝了一個函式 就是回呼函式
# test("hello") 可以在第一個def用print測試


def test(arg):
  arg("hello")

def handle(da):
    print(da)

test(handle) #利用下面印出上面

print("===========")

def add(n1,n2,cb):
    cb(n1+n2)

def handle(result):
  print("結果是",result)

add(3,4,handle) #順序暫時理解不能