#儲存檔案
# file=open("data.txt",mode="w", encoding="utf-8") #開啟
# file.write("Hello File\nSecond Line\n測試中文") #操作
# file.close() #關閉

# with open("data.txt", mode="w",encoding="utf-8") as file:
#     file.write("測試中文\n好棒")
with open("data.txt", mode="w",encoding="utf-8") as file:
    file.write("5\n3")

#讀取檔案
#把檔案中的數字資料,一行一行的讀取出來,並計算總和
sum=0
with open("data.txt", mode="r",encoding="utf-8") as file:
    for line in file: #一行一行的讀取
        sum+=int(line)
print(sum)
# with open("data.txt", mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

#使用JSON格式,複寫
import json 
with open("config.json", mode="r") as file:
    data=json.load(file) #data是字典資料
data["name"]="New name" #修改變數資料

with open("config.json",mode="w")as file:
    json.dump(data,file)
print("name:",data["name"])
print("version:",data["version"])