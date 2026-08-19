n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def lower_bound(target):
    left = 0
    right = n-1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target: # target 이상인 경우
            right = mid - 1    # 더 왼쪽을 탐색하도록 하여 lower_bound를 탐색
        else:
            left = mid + 1
    
    return left

def upper_bound(target):
    left = 0
    right = n-1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
    
for target in queries:
    print(upper_bound(target) - lower_bound(target))