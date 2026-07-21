n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 격자의 가장 바깥 부분은 항상 빙하가 아니며 (0), 빙하로 둘러쌓인 물은 녹이지 않는다. -> (0,0)을 시작으로 BFS로 녹일 부분 탐색.
# 빙하를 녹일 때는, 먼저 0을 기준으로 녹일 빙하 영역 + 갯수 카운팅하고, 모두 탐색 마친 후에 녹일 것.

from collections import deque

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()

    visited[0][0] = True
    q.append((0,0))

    melt_list = []

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True

                if a[nx][ny]:
                    melt_list.append((nx, ny))
                else:
                    q.append((nx, ny))
    return melt_list

time = 0
last_cnt = 0

while True:
    melt = bfs()

    if not melt:
        break
    
    last_cnt = len(melt)
    for x, y in melt:
        a[x][y] = 0

    time += 1

print(time, last_cnt)