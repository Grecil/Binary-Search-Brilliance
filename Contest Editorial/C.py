from bisect import bisect_left as bsl
from bisect import bisect_right as bsr
from collections import defaultdict

n = int(input())
arr = [int(i) for i in input().split()]
indices = defaultdict(list)
for i in range(n):
    indices[arr[i]].append(i + 1)
k = int(input())
for i in range(k):
    l, r, x = map(int, input().split())
    left = bsl(indices[x], l)
    right = bsr(indices[x], r)
    print(right - left)
