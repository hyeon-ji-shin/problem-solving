# 일일이 가격이 떨어지지 않은 기간을 구하지 않고,
# '스택'을 통해 가격이 아직 안 떨어진 '인덱스'를 저장하여, 가격이 떨어지면 기간을 구하여 answer 확정시키기
    
def solution(prices):
    n = len(prices)
    answer = [0] * n # 가격이 떨어지지 않은 기간을 저장할 배열
    stack = [] # 스택을 이용하여 이전 가격과 현재 가격 비교
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            # i 시점의 가격이 현재 스택의 top 인덱스 가격보다 낮다면: 가격이 떨어졌으므로, 기간 계산
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    
    # 스택이 남아 있다면: 가격이 떨어지지 않은 경우이므로 최종적으로 기간 계산
    while stack:
        prev = stack.pop()
        answer[prev] = n - 1 - prev
        
    return answer