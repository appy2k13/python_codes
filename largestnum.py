def realsort(l1):
    i = 1
    while i < len(l1):
        if len(l1[i -1]) > len(l1[i]):
            num1 = ""
            num2 = ""
            for j in l1[i-1]:
                num1 = num1+str(j)
            for k in l1[i]:
                num2 = num2+str(k)
            j = int(num1+num2)
            k = int(num2+num1)
            if j<k:
                j = l1[i-1]
                l1[i-1] = l1[i]
                l1[i] = j
                if i!=1:
                    i = i-2
        i = i+1
    return l1
n = int(input())

lst = list(map(int,input().split()))
l1 = []
for i in lst:
    l = []
    while i > 0:
        l.insert(0,i%10)
        i = int(i/10)
        l2 = tuple(l)
    l1.append(l2)
l1.sort(reverse = True)
l1 = realsort(l1)
st = ""
for i in l1:
    for j in i:
        st = st + str(j)
print(int(st))
