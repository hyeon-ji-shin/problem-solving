n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_move(x, y):
    if grid[x][y] != 1:
        return True
    return False

def bfs(i, j):
    q = deque()
    
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]

    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if is_valid(nx, ny) and not visited[nx][ny] and can_move(nx, ny):
                if grid[nx][ny] == 3:
                    return dist[x][y] + 1
                q.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
    return -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            print(bfs(i, j), end=' ')
        else:
            print(0, end=' ')
    print()