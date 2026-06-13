import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans_k = 1
ans_area = 0

dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j):
    visited[i][j] = True
    for k in range(4):
        new_x, new_y = i + dx[k], j + dy[k]
        if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] > K:
            dfs(new_x, new_y)

for K in range(1, 101):
    # visited / 안전 영역 초기화
    visited = [[False] * m for _ in range (n)]
    area = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and grid[i][j] > K:
                dfs(i, j)
                area += 1
    # 만약 더 많은 안전 영역을 갖는 K의 경우가 발견되면 업데이트
    if area > ans_area:
        ans_area = area
        ans_k = K

print(ans_k, ans_area)