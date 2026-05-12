import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 그래프
graph = [[] for _ in range(n+1)]

for a, b, w in edges:
    graph[a].append((b,w))

INF = int(1e9)

# 최단거리 배열
dist = [INF] * (n+1)

# 시작점
dist[1] = 0

# 우선순위 큐
pq = []

# (거리, 정점)
heapq.heappush(pq, (0, 1))

while pq:
    #가장 거리 작은 정점 꺼내기
    cur_dist, u = heapq.heappop(pq)

    #이미 더 짧은 거리로 방문한 적 있으면 Skip
    if cur_dist > dist[u]:
        continue
    
    #연결된 정점 확인
    for v, w in graph[u]:

        new_dist = cur_dist + w

        # 더 짧은 경로 발견 시 업데이트 및
        if new_dist < dist[v]:
            dist[v] = new_dist

            heapq.heappush(pq, (new_dist, v))

for i in range(2, n+1):
    
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])

