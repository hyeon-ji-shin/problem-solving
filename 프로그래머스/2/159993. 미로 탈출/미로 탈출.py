from collections import deque

def is_valid_move(ny, nx, n, m, maps):
    # 다음 위치는 맵 상에 있어야 하며, X면 안됨.
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

def append_to_queue(ny, nx, k, time, visited, q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time+1)) #(다음 위치(ny, nx), 레버 당김 유무, 현재까지 이동 횟수)

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    # 위, 아래, 왼쪽, 오른쪽 방향
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque( )
    end_y, end_x = -1, -1
    
    # 시작점과 도착점을 찾아두기, 시작점 큐에 넣고 방문 여부 표시
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                q.append((i, j, 0, 0)) # 시작점
                visited[i][j][0] = True
            if maps[i][j] == "E":
                end_y, end_x = i, j # 도착점
    
    # 이동하면서 계산
    while q:
        y, x, k, time = q.popleft( ) # 큐에서 좌표와 이동 횟수를 꺼냄
        
        if y == end_y and x == end_x and k ==1: # 끝 지점에 도착했으며, 레버를 당긴 상태일 때
            return time
        
        # 네 방향 모두 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 이동가능한 경우 큐에 추가
            if not is_valid_move(ny, nx, n, m, maps):
                continue
            
            # 레버를 찾았을 때
            if maps[ny][nx] == "L":
                append_to_queue(ny, nx, 1, time, visited, q)
            # 다음 이동 지점이 레버가 아닐 때
            else:
                append_to_queue(ny, nx, k, time, visited, q)
                
    # 도착점에 도달하지 못하고 q가 빌 경우(이동 가능한 곳을 다 방문했을 때),
    return -1