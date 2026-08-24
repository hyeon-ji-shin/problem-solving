n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
left = 0
right = max(x2 for x1, x2 in segments)

segments.sort()

def check_segments(mid):
    prev = segments[0][0]
    for x1, x2 in segments[1:]:
        if x1 > prev+mid:
            cur = x1
        else:
            cur = prev+mid
        
        if not x1 <= cur <= x2:
            return False

        prev = cur

    return True

while left <= right:
    mid = left + (right - left) // 2
    
    if check_segments(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)