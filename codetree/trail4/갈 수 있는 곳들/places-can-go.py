n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def bfs():
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            if can_go(new_x, new_y):
                visited[new_x][new_y]= True
                q.append((new_x, new_y))

q = deque()
visited = [[False] * n for _ in range(n)]

for i in range(k):
    x, y = points[i]
    x -= 1
    y -= 1
    visited[x][y] = True
    q.append((x, y))
bfs()

ans = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            ans += 1
print(ans)

    
