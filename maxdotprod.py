n = int(input())
ads = list(map(int, input().split()))
clks = list(map(int, input().split()))
ads.sort()
clks.sort()
val = 0
for i in range(n):
    val = val+(ads[i]*clks[i])
print(val)
