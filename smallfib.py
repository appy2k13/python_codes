n = int(input())
if n == 0:
    print(0)
elif n == 1 :
    print(1)
else:
    pn = 0
    pnn = 1
    pnew = 0
    for i in range(n - 1):
        pnew = pn + pnn
        pn = pnn
        pnn = pnew
    print(pnn)
