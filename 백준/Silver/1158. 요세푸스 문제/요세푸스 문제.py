from collections import deque

n, k = map(int, input().split())

q = deque(range(1,n+1))
result = []


while q:
    # 원형 큐처럼 구현하기 위해, k-1번째까지는 front에서 팝하고 rear에 푸시
    for _ in range(k-1):
        q.append(q.popleft()) 
    # k번째 데이터를 팝해서 result에 푸시
    result.append(q.popleft())
    
print('<' + ', '.join(map(str, result)) + '>')