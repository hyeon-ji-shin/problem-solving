def solution(clothes):
    
    # 옷 종류별 개수를 세기 위해 '해시' 사용
    # {
    #   "headgear": 2,
    #   "eyewear": 1
    # }
    
    clothes_dict = {}
    
    # 1. 옷 종류별 개수 세기
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    # 2. 조합 계산
    answer = 1
    
    for count in clothes_dict.values():
        answer *= (count+1)
        
    return answer - 1 # 아무것도 안 입는 케이스 제외