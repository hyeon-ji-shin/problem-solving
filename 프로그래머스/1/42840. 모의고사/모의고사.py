def solution(answers):
    
    # 각 학생별 답안 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 각 학생별 점수 담을 배열 선언
    scores = [0] * 3
    
    # 각 학생별 점수 계산
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j] += 1
    
    # 동점자 발생을 고려하여, 최고점을 파악한 후 가장 많은 문제를 맞힌 사람 append
    max_score = max(scores)
    answer = []
    
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i+1) # 배열 인덱스와 학생 번호 차이 고려해서 +1
            
    return answer