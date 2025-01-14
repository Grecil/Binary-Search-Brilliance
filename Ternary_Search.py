n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
print(*list(range(n)), sep=" ")

while right - left >= 3:
    # Divide array into three parts
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Compare values at mid points
    if arr[mid1] > arr[mid2]:
        # Peak lies in left segment
        right = mid2
    else:
        # Peak lies in right segment
        left = mid1

# Find maximum in remaining small segment
peak = max(arr[left : right + 1])
print(peak)
