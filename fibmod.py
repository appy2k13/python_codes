m, n = list(map(int,input().split()))
if m==0:
    print(0)
elif m==1:
    print(1)
else:
    pn = 0
    pnn = 1
    flag = 0
    l1 = 0
    l2 = 1
    lst = list()
    lst.append(0)
    lst.append(1)
    index = 2
    for i in range(m - 1):
        pnew = pn + pnn
        pn = pnn
        pnn = pnew
        lst.append(pnew%n)
        index = index+1
        if lst[index-2] == 0 and lst[index-1] == 1 :
            flag = 1
            lst.pop(index-1)
            lst.pop(index-2)
            index = index - 2
            break
    if flag == 1:
        t = m%(index)
        print(lst[t])
    else:
        print(pnew%n)
