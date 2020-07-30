arr = list(map(int,input().split()))
qrr = list(map(int,input().split()))

n=arr[0]
q=qrr[0]

def binser(arr, el, l, h):
    if h<l:
        return 0
    mid = int((l+h)/2)
    if el == arr[mid]:
        return mid
    elif el > arr[mid]:
        return binser(arr, el, mid+1, h)
    else:
        return binser(arr, el, l, mid-1)

i = 1
res = []
while i<=q:
    temp = binser(arr, qrr[i], 1, n)
    res.insert(i-1,temp-1)
    i = i+1
print(*res)
