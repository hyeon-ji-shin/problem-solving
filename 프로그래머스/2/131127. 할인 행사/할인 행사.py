def solution(want, number, discount):
    want_dict = {}
    
    # 원하는 제품 목록에 대한 딕셔너리 추가
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    answer = 0 # 원하는 제품을 모두 할인받는 총 일수를 저장할 변수
    
    for i in range(len(discount) - 9):
        can_buy = {}
        for j in range(i, i+10):
            if discount[j] in want_dict: # 구매하려는 목록에 있는 물건이라면, 딕셔너리 값 추가
                can_buy[discount[j]] = can_buy.get(discount[j], 0) + 1
        if want_dict == can_buy:
            answer += 1
    return answer