def swap(a,b):
    if a<b:
        b=a+b
        a=b-a
        b=b-a
    return(a,b)
a, b = list(map(int,input().split()))
(a,b) = swap(a,b)
while a%b!=0 :
    a=a%b
    (a,b)=swap(a,b)
print(b)
