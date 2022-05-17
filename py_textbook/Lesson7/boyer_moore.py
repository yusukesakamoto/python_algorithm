text = "I'm Pyt learning Python.It's interesting!"
pattern = "Python"
tn = len(text)
pn = len(pattern)

skip = [pn]*256
for i in range(pn-1):
    print(ord(pattern[i]))
    print("値",(pn-i-1))
    o = ord(pattern[i])
    skip[o] = pn-i-1

flg = False
p = pn - 1
while p < tn:
    flg = True
    for i in range(pn):
        if text[p-i] != pattern[pn-1-i]:
            flg = False
            break
    if flg == True:
        break
    print(p)
    print(skip[ord(text[p])])
    p += skip[ord(text[p])]

print(text)
if flg == True:
    print(str(p+1-(pn-1))+"文字目に"+pattern+"があります")
else:
    print(pattern+"は見つかりませんでした")