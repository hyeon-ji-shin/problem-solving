def solution(citations):
    
    citations.sort(reverse=True) # [3,0,6,1,5] -> [6,5,3,1,0]으로 정렬
    
    # citation[i] : (i+1)번째로 많이 인용된 논문
    
    # (i+1)개의 논문이 (i+1) 이상 인용되었는 가를 찾으므로, 조건이 깨질 때 직전 i로 answer 결정
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        
    # 반복문을 모두 돌았을 때 조건이 깨지지 않았으므로, 모든 논문이 len(citations) 이상 인용된 것임.
    return len(citations)