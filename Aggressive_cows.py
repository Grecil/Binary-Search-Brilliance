def can_place_cows(stalls, n, cows, min_dist):
    count = 1
    last_pos = stalls[0]
    for i in range(1, n):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]
            if count >= cows:
                return True
    return False


n, k = map(int, input().split())
stalls = list(map(int, input().split()))
stalls.sort()

left = 0
right = stalls[n - 1] - stalls[0]  # Maximum possible distance
result = 0

while left <= right:
    mid = (left + right) // 2

    # If we can place k cows with this distance, try larger distance
    if can_place_cows(stalls, n, k, mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
