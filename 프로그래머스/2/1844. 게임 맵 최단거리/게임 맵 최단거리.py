from collections import deque

def solution(maps):
    # 이동 방향 4가지 선언
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    
    n = len(maps)    # 행
    m = len(maps[0]) # 열
    
    # 거리를 저장하는 배열 dist를 -1로 초기화
    dist = [[-1] * m for _ in range(n)]
    
    # BFS 함수 선언
    def bfs(start):
        
        # 시작지점과 시작지점에서 거리 반영
        q = deque([start])
        dist[start[0]][start[1]] = 1
        
        # deque가 빌 때까지
        while q:
            current = q.popleft()
            
            # 현재 위치에서 이동할 수 있는 모든 방향
            for direct in move:
                row, column = current[0] + direct[0], current[1] + direct[1]
                
                if row < 0  or row >=n or column < 0 or column >= m:
                    continue
                
                if maps[row][column] == 0:
                    continue
                
                if dist[row][column] == -1:
                    q.append([row, column])
                    dist[row][column] = dist[current[0]][current[1]] + 1
        return dist
    
    bfs([0, 0])
    
    return dist[n-1][m-1]