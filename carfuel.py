d = int(input())
m = int(input())
n = int(input())
lst = list(map(int,input().split()))
lst.append(d)
lst.insert(0,0)
current = 0
count = -1
i = 0
while i <= n:
    if lst[i+1] - current > m :
        count = -1
        break
    count = count + 1
    while i<=n and lst[i+1]-current<=m :
        i=i+1
    current = lst[i]
print(count)
