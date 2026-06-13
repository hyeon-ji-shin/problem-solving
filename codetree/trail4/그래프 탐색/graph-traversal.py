n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]
ans = 0

def dfs(vertex):
    global ans

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            dfs(curr_v)

for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(ans)