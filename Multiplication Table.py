n, m, k = map(int, input().split())

low, high = 1, n * m
while low < high:
    mid = (low + high) // 2
    count = 0
    # For each row i, count numbers <= mid by taking min of: column count (m) or mid/i
    for i in range(1, n + 1):
        count += min(m, mid // i)
     # If we haven't found k numbers yet, search upper half; otherwise search lower half
    if count < k:
        low = mid + 1 
    else: 
        high = mid

print(low)
