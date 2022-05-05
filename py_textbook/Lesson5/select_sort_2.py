data = [6,3,7,1,4,2,5,8,9,0]
print(data,"元のデータ")

for i in range(0,9):
    m = i
    for j in range(i+1,10):
        if data[j] < data[m]:
            m = j #jの一周が毎回最小値を導き出している。　
    data[i],data[m] = data[m],data[i]
    print(data,i+1) #過程の出力
    
print(data,"ソート後のデータ")