def swap(a,b):
    if a<b:
        b=a+b
        a=b-a
        b=b-a
    return(a,b)
a, b = list(map(int,input().split()))
(m,n) = swap(a,b)
while m%n!=0 :
    m=m%n
    (m,n)=swap(m,n)
lcm=int((a*b)/n)
print(lcm)
