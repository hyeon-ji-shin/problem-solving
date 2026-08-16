n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False] * n for _ in range(n)]
answer = [[-1] * n for _ in range(n)]

q = deque()

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
            answer[i][j] = 0
            visited[i][j] = True

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y = q.popleft()

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            if grid[nx][ny] == 1:
                answer[nx][ny] = answer[x][y] + 1
                q.append((nx, ny))
                visited[nx][ny] = True

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and not visited[i][j]:
            print(-2, end=' ')
        else:
            print(answer[i][j], end=' ')
    print('')