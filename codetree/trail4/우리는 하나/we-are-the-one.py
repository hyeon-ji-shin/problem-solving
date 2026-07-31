n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[False] * n for _ in range(n)]

# 인접한 도시 간의 이동이 양방향으로 가능하다는 것을 고려하면,
# 각 도시를 연결 요소가 있는 그룹으로 묶고,
# 각 그룹의 도시 하나씩만 선택하면, 같은 그룹 내 다른 도시를 선택해도 그 뒤로 이동가능 도시 수는 늘어나지 않음.

# 즉, 연결 요소가 많은 그룹 순서대로, 그룹별 임의의 도시 하나를 선택하면 되는 것이고,
# 결과적으로, 연결 요소가 많은 그룹 순서대로, 연결 요소 수를 합하는 것이 출력이 된다.

def can_move(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    count = 1

    while q:
        x, y = q.popleft()

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if not can_move(nx, ny):
                continue
            
            if visited[nx][ny]:
                continue
            
            diff = abs(grid[x][y] - grid[nx][ny])

            if u <= diff <= d:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
        
    return count

components = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = bfs(i, j)
            components.append(size)

components.sort(reverse=True)

print(sum(components[:k]))