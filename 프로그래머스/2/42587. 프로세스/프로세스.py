from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    count = 0
    
    while q:
        # 큐에서 하나를 꺼낸다
        cur = q.popleft()
        
        # 더 높은 우선순위가 있다면 뒤로 보낸다
        if q and cur < max(q):
            q.append(cur)
        # 없으면 count += 1
        else:
            count += 1
            # 만약 count하고자 하는 위치로 왔다면 return
            if location == 0:
                return count
        # 가장 앞 숫자 처리했으므로 location -=1 처리
        location -= 1
        
        # 내 프로세스가 앞에 있었는데 뒤로 밀려났을 경우를 처리하기 위해 len(q)-1로 다시 정상화
        if location < 0:
            location = len(q) - 1