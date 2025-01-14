from bisect import bisect_left as bsl
from bisect import bisect_right as bsr

n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
k = int(input())
ans = []
for i in range(k):
    l, r = map(int, input().split())
    left = bsl(arr, l)
    right = bsr(arr, r)
    ans.append(right - left)
print(*ans)
