n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
INF = sys.maxsize

dp = [ [INF] * n for _ in range(n)]

dp[0][0] = grid[0][0]

# initialize
for i in range(1, n):
    dp[i][0] = max(grid[i][0], dp[i-1][0])

for j in range(1, n):
    dp[0][j] = max(grid[0][j], dp[0][j-1])

# dp
for i in range(1, n):
    for j in range(1, n):
        if dp[i][j] != INF:
            continue
        
        dp[i][j] = max(grid[i][j], min(dp[i-1][j], dp[i][j-1]))

print(dp[n-1][n-1])
