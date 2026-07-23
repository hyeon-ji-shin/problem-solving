n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * n for _ in range(n)]

# dp[i][j] : maximum of sum from (0,0) to (i,j)
dp[0][0] = grid[0][0]

# initialization (first row)
for j in range(1,n):
    dp[0][j] = dp[0][j-1] + grid[0][j]
# initialization (first column)
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]

print(dp[n-1][n-1])