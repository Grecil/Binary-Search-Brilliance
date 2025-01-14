from bisect import bisect_right as bsr


def find_num(x):
    low = 1
    high = 10**18
    while low <= high:
        mid = low + (high - low) // 2
        if nums_not_in_list(mid) < k:
            low = mid + 1
        else:
            high = mid - 1
    return low


n, q = map(int, input().split())
arr = [int(i) for i in input().split()]
nums_not_in_list = lambda x: x - bsr(arr, x)
for i in range(q):
    k = int(input())
    print(find_num(k))
