# 이 시간 안에 n명을 처리할 수 있는가? 여부로 이분탐색하기.
# n분이 있을 때, A 심사관은 n//7명 + B 심사관은 n//10명을 심사할 수 있다.

# 최소 시간 : 1, 최대 시간 : max(times)*n, 중간 시간 sum(mid//time)

def solution(n, times):
    
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left+right)//2
        
        people = 0
        
        for time in times:
            people += mid // time
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid +1
            
    return answer