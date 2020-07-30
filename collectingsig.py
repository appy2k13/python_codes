n = int(input())
lst = list()
for i in range(n):
    (a,b) = tuple(map(int,input().split()))
    lst.append((a,b))
lst1 = list()
for (a,b) in lst:
    lst1.append((b,a))
lst1.sort()
lst = []
for (a,b) in lst1:
    lst.append((b,a))
count = 0
cord = list()
i = 0
while i<n:
    (a,b) = lst[i]
    cord.append(b)
    count = count+1
    while i<n-1:
        (a1,b1)=lst[i+1]
        if a1>b:
            break
        else:
            i=i+1
    i=i+1
print(count)
print(*cord)
