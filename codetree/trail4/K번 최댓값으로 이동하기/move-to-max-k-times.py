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

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start_r, start_c):
    best_value = -1
    best_r = -1
    best_c = -1
    
    q = deque()
    visited = [[False]*n for _ in range(n)]
    
    visited[start_r][start_c] = True
    q.append((start_r, start_c))
    start_value = grid[start_r][start_c]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            # 만약, can_go가 안되면 그냥 loop 탈출하기.
            if can_go(nx, ny, start_value) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

                # queue 중에서 가장 큰 값들을 남김. + 그 값의 위치로 저장하기
                # queue 중에서 가장 큰 값이 여러개면, 더 작은 행/열 위치에 있는 값으로 현재 위치 바꾸기. + 탐색 수 늘리기.

                if grid[nx][ny] > best_value:
                    best_value = grid[nx][ny]
                    best_r = nx
                    best_c = ny
                elif grid[nx][ny] == best_value:
                    if nx < best_r:
                        best_r = nx
                        best_c = ny
                    elif nx == best_r:
                        if ny < best_c:
                            best_r = nx
                            best_c = ny            

    return best_r, best_c    

for _ in range(k):
    nx, ny = bfs(curr_r, curr_c)

    if nx == -1:
        break
    curr_r, curr_c = nx, ny

print(curr_r+1, curr_c+1)