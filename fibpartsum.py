m, n = list(map(int,input().split()))
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
qm = int((m-1)/index)
rm = int((m-1)%index)
qn = int(n/index)
rn = int(n%index)
#print(qm,rm,qn,rn)
lstsum = 0
rnsum = 0
rmsum = 0
for i in range(index):
    #print (i)
    lstsum = lstsum + lst[i]
    if i<=rm:
        rmsum = rmsum + lst[i]
    if i<=rn:
        rnsum = rnsum + lst[i]
msum = qm*lstsum + rmsum
nsum = qn*lstsum + rnsum
sum = (nsum-msum)%10
print(sum)
