def can_ship(capacity):
    days = 1
    current_weight = 0
    for weight in weights:
        if current_weight + weight > capacity:
            days += 1
            current_weight = 0
        current_weight += weight
    return days > D


n, D = map(int, input().split())
weights = [int(i) for i in input().split()]
low = max(weights)
high = sum(weights)
while low <= high:
    mid = low + (high - low) // 2
    if can_ship(mid):
        low = mid + 1
    else:
        high = mid - 1
print(low)
