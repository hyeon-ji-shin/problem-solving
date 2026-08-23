n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# Please write your code here.
left = 1
right = max(arr) * n

while left<=right:
    mid = left + (right - left) // 2
    
    cnt_total_exit = 0
    for exit in arr:
        cnt_total_exit += mid // exit
    
    if cnt_total_exit >= n:
        right = mid - 1
    else:
        left = mid + 1

print(right+1)