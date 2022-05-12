#載入sys模組並取得資訊
import sys as s #模組,載入使用
print(s.platform)
print(s.maxsize)

#調整搜尋模組的路徑
import sys
sys.path.append("modules") 
print(sys.path)#印出模組的搜尋路徑

#使用sys模組
#建立geometry模組,載入使用
import geometry
result=geometry.distance(1,1,5,5)
print(result)
import geometry
result=geometry.slope(1,1,5,5)
print(result)
