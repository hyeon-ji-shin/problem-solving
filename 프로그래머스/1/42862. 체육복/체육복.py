def solution(n, lost, reserve):
    
    # 여벌을 갖고 있는 도난 당한 학생을 미리 처리
    lost = set(lost)
    reserve = set(reserve)
    both = lost & reserve
    
    lost -= both
    reserve -= both
    
    # 도난 당한 학생 주위로 여벌 있는지 확인
    for number in sorted(lost):
        if number-1 in reserve:
            reserve.remove(number-1)
        elif number+1 in reserve:
            reserve.remove(number+1)
        else:
            n -= 1
    return n