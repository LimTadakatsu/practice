# #網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學的原始碼 (html css js)
# print(data)

#串接、擷取公開資料

import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(src) as response:
#      data=response.read().decode("utf-8") #取得網站原始碼 (html css js)
with request.urlopen(src) as response:
    data=json.load(response)
print(data)
#將公司名稱列表出來
clist=data["result"]["results"]
#     for company in clist:
# print(company["公司名稱"])
with open("data_for_api.txt","w",encoding="utf-8") as file:
    for company in clist:
      file.write(company["公司名稱"]+"\n")