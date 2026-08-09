n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
from collections import deque

q = deque()
visited = [ [[False] * (k + 1) for _ in range(n)] for _ in range(n)]
dist = [ [[0] * (k+1) for _ in range(n)] for _ in range(n)]
q.append((r1, c1, 0))
visited[r1][c1][0] = True

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = -1

while q:
    x, y, broken = q.popleft()

    if x == r2 and y == c2:
        answer = dist[x][y][broken]
        break

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if visited[nx][ny][broken]:
            continue
        if grid[nx][ny]:
            if broken < k:
                q.append((nx,ny,(broken+1)))
                visited[nx][ny][(broken+1)] = True
                dist[nx][ny][(broken+1)] = dist[x][y][broken] + 1
        else:
            q.append((nx,ny,broken))
            visited[nx][ny][broken] = True
            dist[nx][ny][broken] = dist[x][y][broken] + 1

print(answer)