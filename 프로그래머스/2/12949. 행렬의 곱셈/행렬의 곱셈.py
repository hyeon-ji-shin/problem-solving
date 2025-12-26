def solution(arr1, arr2):
    # 2차원 행렬 곱을 계산해보자.
    
    # arr2의 열 분리
    arr2_cols = list(zip(*arr2)) # 열 추출 [(1, 4), (2, 5), (3, 6)]
    
    answer = []
    
    for row in arr1:
        temp_row = []
        for col in arr2_cols:
            s = 0
            # 같은 위치 원소를 하나씩 꺼내서 묶은 후 벡터 내적
            for a, b in zip(row, col): 
                s += a * b
            temp_row.append(s)
        answer.append(temp_row)
            
    return answer

