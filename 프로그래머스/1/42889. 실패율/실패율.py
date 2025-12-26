def solution(N, stages):
    # 각 스테이지에서 멈춘 사람 수
    stuck_cnt = [0] * (N+2)
    for stage in stages:
        stuck_cnt[stage] += 1
    
    # 각 스테이지별 실패한 사용자 수
    failure = {}
    player_cnt = len(stages) # 일단 전체 플레이어 수로 표현, 이후 실패율 계산 순회 과정에서 각 스테이지에서 멈춘 사람을 빼는 식으로 반영.
    
    # 각 스테이지별 실패율 계산
    for i in range(1, N+1):
        if stuck_cnt[i] == 0:
            failure[i] = 0
        else:
            failure[i] = stuck_cnt[i] / player_cnt
            player_cnt -= stuck_cnt[i]
    
    answer = sorted(failure, key=lambda x: failure[x], reverse=True)
    return answer