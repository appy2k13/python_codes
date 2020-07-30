n = int(input())
lst = list(map(int,input().split()))
if n != len(lst) :
    print("Input mismatch")
    exit()

if n == 2 :
    print(lst[0]*lst[1])
    exit()
big1 = 0
big2 = 1
for i in range(n) :
    if lst[i] > lst[big1] :
        big2 = big1
        big1 = i
    elif lst[i] > lst[big2] :
        big2 = i
    else :
        continue
if big1 != big2 :
    print(lst[big1]*lst[big2])
