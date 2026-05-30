n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
import heapq
import sys

INF = sys.maxsize

graph = [[] for _ in range(n+1)]

# 인접 그래프 생성
for u, v, w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w)) # 양방향

# 거리 배열 생성
dist = [INF] * (n+1)
# parent 배열 생성
parent = [0] * (n+1) # 최단 경로에서 i 직전의 정점

# 시작 정점 설정
pq = []
dist[A] = 0
heapq.heappush(pq, (0, A)) # 자기 자신까지 거리는 0.

# Dijkstra
while pq:
    cur_dist, cur = heapq.heappop(pq) # 가장 가까운 정점 꺼내기

    # 오래된 정보 무시
    if cur_dist > dist[cur]:
        continue
    
    # 인접 정점 탐색
    for nxt, cost in graph[cur]:
        new_dist = cur_dist + cost
        if new_dist < dist[nxt]:
            dist[nxt] = new_dist # 최단 거리 업데이트
            parent[nxt] = cur # 이전 정점 인덱스 저장
            heapq.heappush(pq, (new_dist, nxt)) # 새로운 후보를 힙에 넣음

# 경로 복원
path = []
cur = B

# 목적지에서부터 거꾸로
while cur:
    path.append(cur)
    if cur == A:
        break
    cur = parent[cur]

path.reverse()

print(dist[B])
print(*path)