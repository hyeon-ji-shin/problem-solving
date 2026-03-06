def solution(numbers):
    
    # 문자열은 사전식 비교
    # numbers의 원소가 1000 이하이므로, 더 작은 자릿수의 숫자들도 x*3으로 늘려서 비교 (e.g., 3, 30에 대하여: 333 303030 -> 3 채택)
    
    # 1. 숫자를 문자열로 변환 [6, 10, 2] -> ['6', '10', '2']
    numbers = list(map(str, numbers))
    
    # 2. 정렬 ('666', '101010', '222' 기준으로)
    numbers.sort(key=lambda x: x*3, reverse=True) # 큰값이 먼저 오도록
    
    # 3. 문자열 합치기
    answer = ''.join(numbers)
        
    return str(int(answer)) # 00 > 0 예외처리