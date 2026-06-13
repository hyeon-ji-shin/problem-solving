n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0 for _ in range(m)] for _ in range(n)]

def is_valid(x, y):
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    
    if grid[x][y] == 0 or visited[x][y]:
        return False
    
    return True

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if is_valid(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])
