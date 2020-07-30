n = int(input())

def fibmod(n):
    if n == 0:
        return (0,1)
    elif n == 1:
        return (1,1)
    else:
        pn = 0
        pnn = 1
        sum = 1
        lst = list()
        lst.append(0)
        lst.append(1)
        index = 2
        flag = 0
        while (1):
            pnew = pn + pnn
            pn = pnn
            pnn = pnew
            sum = (sum+pnn)%10
            lst.append(pnew%10)
            index = index+1
            if lst[index-2] == 0 and lst[index-1] == 1 :
                lst.pop(index-1)
                lst.pop(index-2)
                index = index-2
                break
        m = n+1
        rm = int(m%index)
        rn = int(n%index)
        pn = lst[rn]
        pnn = lst[rm]
        return (pn,pnn)
(a,b) = fibmod(n)
print((a*b)%10)
