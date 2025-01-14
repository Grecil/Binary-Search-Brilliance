_, goal = map(int, input().split())
machines = list(map(int, input().split()))

lo = 1
hi = int(1e9)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    # Calculate total items produced by all machines in 'mid' time
    n_produced = 0
    for machine in machines:
        n_produced += mid // machine
        # If we can produce enough items, try to minimize time
    if n_produced >= goal:
        ans = mid
        hi = mid - 1
    # If we can't produce enough, need more time
    else:
        lo = mid + 1
print(ans)
