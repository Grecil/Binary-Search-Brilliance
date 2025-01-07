def lower_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
            
    return left

n, target = map(int, input().split())
arr = list(map(int, input().split()))

lb = lower_bound(arr, target)
ub = upper_bound(arr, target)

print(lb, ub)
