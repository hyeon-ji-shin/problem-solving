n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
INT_MAX = sys.maxsize
MAX_R = 100

dp = [[0] * n for _ in range(n)]

ans = INT_MAX

def initialize():
    # INT_MAX로 초기화
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX
    
    # 시작점의 경우는 dp[0][0] = grid[0][0]으로 초기값을 설정
    dp[0][0] = grid[0][0]

    # 최좌측 열의 초기값을 설정
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], grid[i][0])
    # 최상단 행의 초기값을 설정
    for j in range(1,n):
        dp[0][j] = max(dp[0][j-1], grid[0][j])

def solve(lower_bound):
    # lower_bound 미만 값은 사용할 수 없도록 grid 값 변경
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower_bound:
                grid[i][j] = INT_MAX
    
    # DP 초기화
    initialize()

    # dp 업데이트 : 최대 값의 최소 값
    # [탐색 위치의 값] / [가능한 이전 위치(좌측, 위측) 중 작은 값] 중 최대값
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])
    
    return dp[n-1][n-1]

for lower_bound in range(1, MAX_R+1):
    upper_bound = solve(lower_bound)

    if upper_bound == INT_MAX:
        continue
    ans = min(ans, upper_bound - lower_bound)

print(ans)