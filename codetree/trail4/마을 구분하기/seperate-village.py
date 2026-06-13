n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                cnt += dfs(nx, ny)
    return cnt

# 모든 칸을 시작점 후보로 검사.
for i in range(n):
    for j in range(n):
        # 새로운 마을 발견
        if grid[i][j] == 1 and not visited[i][j]:
            # DFS
            ans.append(dfs(i, j))

# 오름차순 정렬
ans.sort()

print(len(ans))

for x in ans:
    print(x)
