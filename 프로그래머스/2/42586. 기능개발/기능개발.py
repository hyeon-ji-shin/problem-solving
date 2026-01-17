from collections import deque

def solution(progresses, speeds):
    
    answer = []
    q = deque(progresses)
    sp = deque(speeds)
    
    while q:
        # 하루 경과
        for i in range(len(q)):
            q[i] += sp[i]
        
        # 배포 가능한 작업 처리
        cnt = 0
        while q and q[0] >= 100:
            q.popleft()
            sp.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
            
    return answer