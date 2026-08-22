n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
left = 1
right = max(arr)

while left <= right:
    mid = left + (right - left) // 2

    cnt = 0

    for num in arr:
        cnt += (num // mid)
    
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right) # left - 1