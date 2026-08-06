n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False] * m for _ in range(n)]
step = [[-1] * m for _ in range(n)]

def is_valid(x,y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x,y):
    if not is_valid(x,y):
        return False
    if a[x][y] == 0 or visited[x][y]:
        return False
    return True

moves = [(-1, 0), (1, 0), (0, -1), (0,1)]

q = deque()

q.append((0,0))
visited[0][0] = True
step[0][0] = 0

while q:
    x, y = q.popleft()

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if can_go(nx,ny):
            q.append((nx, ny))
            visited[nx][ny] = True
            step[nx][ny] = step[x][y] + 1

print(step[n-1][m-1])