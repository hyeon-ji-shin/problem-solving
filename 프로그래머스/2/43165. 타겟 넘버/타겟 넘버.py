def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer
        
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        # 현재 숫자를 더하는 경우 (e.g. 1번째, 0 + numbers[0])
        dfs(index+1, current_sum + numbers[index])
        
        # 현재 숫자를 빼는 경우   (e.g. 1번째, 0 - numbers[0])
        dfs(index+1, current_sum - numbers[index])
        
    dfs(0, 0)
    
    return answer