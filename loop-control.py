# #break 簡易範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的n
#     n+=1
# print(n)#印出迴圈結束後的n

# continue 的簡易範例
n=0
for x in [0,1,2,3]:
    if x%2==0: # x mod 2 整除2等於0
        continue
    print(x)
    n+1
print("最後的 n:",n)