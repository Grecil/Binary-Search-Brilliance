n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
low = 1
high = 10**9
flag = False
nums_less_than = lambda x: sum(i <= x for i in arr)
while low <= high:
    mid = low + (high - low) // 2
    if nums_less_than(mid) < k:
        low = mid + 1
    else:
        high = mid - 1
print(low if nums_less_than(low) == k else -1)
