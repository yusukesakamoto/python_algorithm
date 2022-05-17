text = "I'm learning Python. It's interesting!"
pattern = "Python"
tn = len(text)
pn = len(pattern)
flg = False
p = 0

while p <= tn-pn:
    c = 0
    for i in range(pn): #位置から６文字分、一文字ずつ照らし合わせて、１文字でも違っていたらbreakで次のマスに行く
        if text[p+i] != pattern[i]:
            break
        c += 1
    if c == pn:
        flg = True
        break
    p += 1

print(text)
if flg == True:
    print(str(p+1)+"文字目に"+pattern+"があります")
else:
    print(pattern+"は見つかりませんでした")