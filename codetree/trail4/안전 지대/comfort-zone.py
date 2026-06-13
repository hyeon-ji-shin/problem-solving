n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

ans_k = 1
ans_area = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and grid[nx][ny] > K
            ):
                visited[nx][ny] = True
                q.append((nx, ny))

for K in range(1, 101):
    visited = [[False] * m for _ in range(n)]
    area = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > K:
                bfs(i, j)
                area += 1

    if area > ans_area:
        ans_area = area
        ans_k = K

print(ans_k, ans_area)