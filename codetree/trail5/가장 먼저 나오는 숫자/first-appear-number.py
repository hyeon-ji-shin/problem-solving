n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
def binary_search(num):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1
    return left

for num in query:
    ans = binary_search(num)
    # lower_bound가 인덱스를 넘긴다(target num보다 큰 값이 arr에 없다)거나, 정확히 타겟값이 arr에 없을 때
    if ans == n or arr[ans] != num: 
        print(-1)
    else:
        print(binary_search(num) + 1)