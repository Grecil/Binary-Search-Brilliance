from bisect import bisect_left as bsl

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])
a, b, p = zip(*arr)
dp = [0] * (n + 1)
for i in range(n):
    #     # Find the latest non-overlapping project before the current one
    x = bsl(b, a[i])
    #     # Maximum profit is either including current project + previous compatible projects,
    #     # or excluding current project
    dp[i + 1] = max(dp[i], dp[x] + p[i])
    print(dp)
print(dp[-1])
