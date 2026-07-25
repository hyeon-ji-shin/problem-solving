n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
sys.setrecursionlimit(10**6)

dp = [[0] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def dfs(x, y):
    # 이미 계산한 경우
    if dp[x][y]:
        return dp[x][y]
    
    # 자기 자신만 방문
    dp[x][y] = 1

    # 상,하,좌,우 탐색
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] > grid[x][y]:
                # grid[nx][ny] 위치보다 지나가는 칸 수가 +1이 되므로
                dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))
    
    return dp[x][y]

answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i,j))

print(answer)
