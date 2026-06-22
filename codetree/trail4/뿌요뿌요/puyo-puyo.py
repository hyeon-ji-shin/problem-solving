n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
block_cnt = 0
block_size_max = 0

visited = [ [False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]
    
        if 0 <= cur_x < n and 0 <= cur_y < n:
            if not visited[cur_x][cur_y] and grid[cur_x][cur_y] == num:
                cnt += dfs(cur_x, cur_y, num)
    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = dfs(i, j, grid[i][j])

            if size >= 4:
                block_cnt += 1
            
            block_size_max = max(block_size_max, size)

print(block_cnt, block_size_max)