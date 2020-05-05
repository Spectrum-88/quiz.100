k = int(input("Enter a number for factorial: "))
# 使用int是絕對必要的，不然會變成文字，無法計算
# 測試中文輸入，可行
result = 1

for i in range( 1, k+1):
    result = result * i

print(result)

