data = [9,4,7,2,3,8,6,1,0,5]
n = len(data)
print(data,"元のデータ")

for i in range(0,n-1):
    for j in range(n-1,i,-1):
        if data[j-1] > data[j]:
            data[j],data[j-1] = data[j-1],data[j]
            print(data,"並び替えの過程")
print(data,"ソート後のデータ")