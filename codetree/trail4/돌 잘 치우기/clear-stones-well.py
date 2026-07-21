n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
from collections import deque
from itertools import combinations

stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i,j))

def is_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if not is_range(x, y):
        return False
    if grid[x][y] == 1:
        return False
    return True

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    max_cnt = -1
    for removed in combinations(stones, m):
        for x, y in removed:
            grid[x][y] = 0

        q = deque()
        visited = [[False] * n for _ in range(n)]
        cnt = 0

        for x, y in zip(r, c):
            if grid[x][y] == 0:
                cnt += 1
                visited[x][y] = True
                q.append((x, y))
        
        while q:
            x, y = q.popleft()
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if can_go(nx, ny) and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
        
        if cnt > max_cnt:
            max_cnt = cnt

        for x, y in removed:
            grid[x][y] = 1

    return max_cnt

print(bfs())  