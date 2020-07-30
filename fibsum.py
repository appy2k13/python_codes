n = int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    pn = 0
    pnn = 1
    sum = 1
    lst = list()
    lst.append(0)
    lst.append(1)
    index = 2
    flag = 0
    for i in range(n-1):
        pnew = pn + pnn
        pn = pnn
        pnn = pnew
        sum = (sum+pnn)%10
        lst.append(pnew%10)
        index = index+1
        if lst[index-2] == 0 and lst[index-1] == 1 :
            lst.pop(index-1)
            lst.pop(index-2)
            flag = 1
            index = index-2
            break
    if flag == 1:
        lstsum = 0
        remsum = 0
        q = int(n/index)
        r = int(n%index)
        for i in range(index):
            lstsum = lstsum + lst[i]
            if i<=r:
                remsum = remsum + lst[i]
        sum = (q*lstsum + remsum)%10
        print(sum)
    else:
        print(sum)
