s = int(input())

# Please write your code here.
# 정렬된 수열에서의 합도 정렬되어 있음. S 이하를 만족하는 범위를 이진탐색으로 upper_bound 찾기.

left = 0
right = 10 ** 18 - 1

def calc_sum(num):
    return (num * (num+1) // 2)

while (left <= right):
    mid = left + (right - left) // 2
    
    if calc_sum(mid) > s:
        right = mid - 1
    else:
        left = mid + 1

print(left-1)