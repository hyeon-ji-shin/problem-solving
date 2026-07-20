n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque

r -= 1
c -= 1
curr_r, curr_c = r, c

def is_range(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True

def can_go(x,y,cur):
    if not is_range(x,y):
        return False
    if grid[x][y] >= cur:
        return False
    return True

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def bfs(start_r, start_c):
    best_value = -1
    best_r = -1
    best_c = -1
    
    q = deque()
    visited = [[False]*n for _ in range(n)]
    
    visited[start_r][start_c] = True
    q.append((start_r, start_c))

    while q:
        curr_r, curr_c = q.popleft()
        for dx, dy in zip(dxs, dys):
            x, y = curr_r + dx, curr_c + dy

            # 만약, can_go가 안되면 그냥 loop 탈출하기.
            if can_go(x, y, grid[start_r][start_c]) and not visited[x][y]:
                visited[x][y] = True
                q.append((x, y))

                # queue 중에서 가장 큰 값들을 남김. + 그 값의 위치로 저장하기
                # queue 중에서 가장 큰 값이 여러개면, 더 작은 행/열 위치에 있는 값으로 현재 위치 바꾸기. + 탐색 수 늘리기.

                if grid[x][y] > best_value:
                    best_value = grid[x][y]
                    best_r = x
                    best_c = y
                elif grid[x][y] == best_value:
                    if x < best_r:
                        best_value = grid[x][y]
                        best_r = x
                        best_c = y
                    elif x == best_r:
                        if y < best_c:
                            best_value = grid[x][y]
                            best_r = x
                            best_c = y            

    return best_r, best_c    

for _ in range(k):
    nx, ny = bfs(curr_r, curr_c)

    if nx == -1:
        break
    curr_r, curr_c = nx, ny

print(curr_r+1, curr_c+1)