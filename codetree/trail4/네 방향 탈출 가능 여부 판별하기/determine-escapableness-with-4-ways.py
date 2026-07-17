n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

q = deque()
visited = [[False] * m for _ in range(n)]
q.append((0, 0))
visited[0][0] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 0:
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
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

bfs()

# 만약 시작 칸에 뱀이 있다면 예외 처리 (현재 문제에서는 해당 X)
# if a[0][0] == 0:
#     print(0)

print(1 if visited[n-1][m-1] else 0)