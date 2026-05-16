n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq
import sys

INT_MAX = sys.maxsize

graph = [[] for _ in range(n+1)]
pq = []

# 각 학생의 등교 최단 거리를 파악해야 하므로,
# 그래프에 있는 모든 노드들에 대해, 초기값을 아주 큰 값으로 설정
dist = [INT_MAX] * (n+1)

# 그래프를 인접리스트로 표현
for x, y, z in edges:
    # 도착 지점(N, 학교)에서 얼마나 걸리는지 파악해야 하므로, 방향 그래프를 반대로 생성
    # 기존 방식: graph[x].append((y, z))
    graph[y].append((x, z))

# 도착 위치를 먼저 0으로 설정
dist[n] = 0

# 우선순위 큐에 도착점 넣기
heapq.heappush(pq, (0, n)) #(거리,vertex 번호)

# O(|E|log|V|)
while pq:
    min_dist, min_index = heapq.heappop(pq)

    # 우선 순위 큐를 이용하면, 같은 정점의 원소가 여러번 들어갈 수 있으므로
    # 현재 파악한 min_dist가 최신 dist[min_index]와 다르면 pass
    if min_dist != dist[min_index]:
        continue
    
    for target_index, target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

# 학교에서 가장 오래 걸리는 학생 파악
longest_dist_index = 1
for i in range(2,n):
    if dist[i] > dist[longest_dist_index]:
        longest_dist_index = i

print(dist[longest_dist_index])