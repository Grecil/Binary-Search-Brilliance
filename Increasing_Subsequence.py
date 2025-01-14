from bisect import bisect_right as bsr
from bisect import bisect_left as bsl

n = int(input())
arr = [int(i) for i in input().split()]

# # dp[i] stores smallest value that can end an increasing subsequence of length i
dp = [float("-inf")] + [float("inf")] * (n + 1)

for i in range(n):
    # Find the position where current element should be inserted to maintain increasing order
    x = bsr(dp, arr[i])
    # If current element can create a better increasing subsequence of length x, update dp
    if dp[x - 1] < arr[i] < dp[x]:
        dp[x] = arr[i]

# First infinity position minus 1 gives the length of longest increasing subsequence
print(bsl(dp, float("inf")) - 1)
