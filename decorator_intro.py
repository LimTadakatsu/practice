#優先呼叫裝飾器再執行一般程式
#callback可以調整執行次序

#定義裝飾器
def myDeco(callback):
    def run():
        print("裝飾器中的程式碼")
        callback(5)
    return run

#使用裝飾器
@myDeco #要使用裝飾器要用@+函式
# def test():
#     print("普通函式")
# test()

def test(n):
    print("普通函式",n)
test()

#定義裝飾器計算1+2+3...+50
def caclulate(callback):
    def run():
        result=0
        for n in range(51):
            result+=n
        callback(result)
    return run

@caclulate
def show(n):
    print("結果是",n)#這邊是普通函式

show()

print("=======")

@caclulate #裝飾器重複利用
def showenglish(n):
    print("result is ",n)
showenglish()