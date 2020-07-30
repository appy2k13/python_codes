n = int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    pn = 0
    pnn = 1
    sum = 1
    for i in range(n-1):
        pnew = pn + pnn
        pn = pnn
        pnn = pnew
        sum = (sum+pnn)
    print(sum)
