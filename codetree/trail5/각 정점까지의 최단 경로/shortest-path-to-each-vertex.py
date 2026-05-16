n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq
import sys

INT_MAX = sys.maxsize

graph = [[] for _ in range(n+1)]
pq = []

# 그래프에 있는 모든 노드들에 대해, 초기값을 아주 큰 값으로 설정
dist = [INT_MAX] * (n+1)

# 그래프를 인접리스트로 표현
for x, y, z in edges:
    graph[x].append((y, z))
    graph[y].append((x, z)) # 무방향 그래프


# 시작 위치는 먼저 0으로 설정
dist[k] = 0

# 우선순위 큐에 시작점 넣기
heapq.heappush(pq, (0, k)) #(거리, vertex 번호)

# O(|E|log|V|) Dijkstra
while pq:
    min_dist, min_index = heapq.heappop(pq)

    # 우선순위 큐를 이용한다면, 같은 정점의 원소가 여러번 들어갈 수 있으므로
    #min_dist가 최신 dist[min_index]와 다르면 Pass시킨다.
    if min_dist != dist[min_index]:
        continue
    
    # 최소값에 해당하는 정점에 연결된 간선들을 따라가며
    # 시작점으로부터 최단거리 값을 갱신한다.
    for target_index, target_dist in graph[min_index]:
        #현재 위치에서 연결된 간선으로 가는 것이 더 작다면
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist # dist 업데이트하고
            heapq.heappush(pq, (new_dist, target_index)) #우선순위 큐에 추가

# 시작점으로부터 각 지점까지의 최단 거리 출력
for i in range(1, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])