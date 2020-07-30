n = int(input())
#print(n)
if n == 0:
    print(0)
elif n == 1:
    print('1')
else:
    pn = 0
    pnn = 1
    for i in range(n - 1):
        pnew = (pn + pnn)%10
        pn = pnn
        pnn = pnew
    print(pnew)
