from math import lcm

n, a, b = map(int, input().split())
low = min(a, b)
high = n * (min(a, b))
count_multiples = lambda x: (x // a) + (x // b) - (x // lcm(a, b))
while low <= high:
    mid = low + (high - low) // 2
    if count_multiples(mid) < n:
        low = mid + 1
    else:
        high = mid - 1
print(low % (10**9 + 7))
