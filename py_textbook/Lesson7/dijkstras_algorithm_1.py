F = 99999
way = [
    [F,3,2,5,F,F,F],
    [3,F,F,F,7,F,F],
    [2,F,F,2,F,4,F],
    [5,F,2,F,F,4,5],
    [F,7,F,F,F,4,5],
    [F,F,4,1,4,F,3],
    [F,F,F,F,5,3,F]
]
dist = [F]*7
flg = [0]*7
start = 0
p = start
dist[p] = 0
print("始点",p)

for i in range(7):
    print(i,"番目");
    d = F
    for j in range(7):
        if flg[j] == 0 and dist[j] < d:
            p = j
            d = dist[j]
            print("p=",p,"d=",dist[j])
    flg[p] = 1
    for k in range(7):
        if dist[p]+way[p][k] < dist[k]:
            print(k,"答え：dk=",dist[k],"dp=",dist[p],"way=",way[p][k])
            dist[k] = dist[p] + way[p][k]
print("各ノードまでの距離")
for i in range(7):
    print("ノード{}まで{}".format(i,dist[i]))