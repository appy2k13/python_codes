def inc(a):
    return(a+1)

n = int(input())
index = 0
lst = [1]
n = n-1
while n>0:
    i = n
    if i<=lst[index]:
        lst[index] = lst[index]+i
        break
    else:
        index = inc(index)
        lst.append(lst[index-1]+1)
        n = n-lst[index]
print(index+1)
print(*lst)
