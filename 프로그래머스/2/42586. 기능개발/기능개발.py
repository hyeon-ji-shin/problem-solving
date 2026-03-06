import math
from collections import deque

def solution(progresses, speeds):

    q = deque()
    
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100-progress)/speed)
        q.append(days)
        
    answer = []
    
    current = q.popleft() # 첫 기능 기준으로 시간
    count = 1
    
    while q:
        if q[0] <= current: # 앞 기능보다 빨리 끝난 경우 같이 배포
            q.popleft()
            count += 1
        else: # 새 배포 시작
            answer.append(count)
            current = q.popleft()
            count = 1
            
    # 마지막 배포까지 반영
    answer.append(count)
    return answer