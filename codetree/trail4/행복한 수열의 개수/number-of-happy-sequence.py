n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

def is_happy_arr(arr):
    cnt = 1
    
    if m==1:
        return True

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            cnt += 1
        else:
            cnt = 1

        if cnt >= m:
            return True
    return False

for row in range(n):
    if is_happy_arr(grid[row]):
        ans += 1

for col in zip(*grid):
    if is_happy_arr(col):
        ans += 1

# for col in range(n):
#     col_arr = [grid[row][col] for row in range(n)]

#     if is_happy_arr(col):
#         ans += 1

print(ans)