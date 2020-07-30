n,w = list(map(int,input().split()))
lst = list()
lstrt = list()
for i in range(n):
    (a,b) = tuple(map(int,input().split()))
    lst.append((a,b))
    lstrt.append((a/b,i))
val = 0.0
lstrt.sort(reverse = True)
for (v,i) in lstrt:
    (a,b) = lst[i]
    if w>b:
        inc = b
    else:
        inc = w
    val = val+(inc*v)
    w = w - inc
    if w == 0:
        break
print(val)
