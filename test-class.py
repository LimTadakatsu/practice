#定義類別、類別屬性(封裝在類別裡的變數和格式) class 屬性
#定義一個類別 IO，有兩個屬性 supporttedSrcs 和 read
class IO:
#類別 IO
#屬性 read supportedSrcs
    supportedSrcs=["console", "file"]
    def read (src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("read from",src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")