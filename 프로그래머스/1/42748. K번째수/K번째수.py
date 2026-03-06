def solution(array, commands):
    
    answer = []
    
    for i, j, k in commands:
        crop = array[(i-1):j] # (i-1) 이상 j 미만
        crop.sort()
        answer.append(crop[k-1])
    
    return answer