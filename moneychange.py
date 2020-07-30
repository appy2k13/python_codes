n = int(input())
c = 0
c = int(n/10)
rem = n%10
if rem >= 5:
    c = c+1
    rem = rem-5
c = c + rem
print(c)
