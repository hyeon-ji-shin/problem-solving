def solution(enroll, referral, seller, amount):
    # parent dictionary의 key는 enroll의 노드, value는 referral의 노드로 구성
    # {
    #   "john" : "-",
    #   "mary" : "-",
    #   "edward" : "mary",
    #   ...
    # }
    parent = dict(zip(enroll, referral))
    
    # 최종 이익금 딕셔너리 생성 및 초기화
    total = {name: 0 for name in enroll}
    
    # seller 리스트와 amount 리스트를 이용해 이익 분배
    for i in range(len(seller)):
        money = amount[i] * 100 # 칫솔 1개당 100원
        cur_name = seller[i]
        # 판매자부터 상위 노드까지 이익 분배
        while money > 0 and cur_name != '-':
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10
    return [total[name] for name in enroll]