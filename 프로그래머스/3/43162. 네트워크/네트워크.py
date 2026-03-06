def dfs(computers, visited, node):
    visited[node] = True
    for idx, connected in enumerate(computers[node]): # enumerate로 현재 node와 연결 여부를 idx와 value로 동시에 꺼내기
        # 연결되어 있으면서 방문하지 않은 노드를 추가 방문
        if connected and not visited[idx]: 
            dfs(computers, visited, idx)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    # 컴퓨터 인덱스 순서대로
    for i in range(n):
        # 아직 방문하지 않은 노드라면 해당 노드로부터 DFS
        if not visited[i]:
            dfs(computers, visited, i)
            answer +=1
    
    return answer