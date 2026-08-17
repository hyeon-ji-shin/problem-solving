n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.


def binary_search(target):
    idx = -1
    left=0
    right=n-1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            idx = mid
            break
        if arr[mid] > target: # 타겟 값이, 현재보다 작다면
            right = mid - 1   # right를 줄이기
        else:
            left = mid + 1 # 타겟 값이 현재보다 크다면, left를 늘리기
    if not idx== -1:
        return (idx+1)
    return idx

for num in queries:
    print(binary_search(num))