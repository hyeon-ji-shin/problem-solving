import math

def solution(progresses, speeds):
    
    answer = []
    n = len(progresses)
    # 각 작업의 배포 가능일 계산
    days_left = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]
    
    cnt = 0
    max_day = days_left[0] # 배포가 되지 않은 가장 앞 순서의 기능의 배포 가능일
    
    for i in range(n):
        if days_left[i] <= max_day: # max_day보다 days_left[i](배포 가능일)가 짧은 기능들은 모두 cnt
            cnt += 1
        else: #현재 max_day보다 긴 days_left를 가진 기능을 만난 경우, answer 추가 + cnt, max_day 업데이트
            answer.append(cnt)
            cnt = 1
            max_day = days_left[i]
    
    answer.append(cnt)
            
    return answer