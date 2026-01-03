def solution(prices):
    n = len(prices)
    answer = []
    
    for i in range(n):
        time = 0
        
        for j in range(i+1, n):
            time += 1
            if prices[j] < prices[i]:
                break
        answer.append(time)
        
    return answer