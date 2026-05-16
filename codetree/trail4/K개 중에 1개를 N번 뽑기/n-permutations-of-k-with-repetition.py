K, N = map(int, input().split())

# Please write your code here.
# 숫자를 고르고 난 다음, 다음 숫자를 고르는 문제가 동일하게 반복된다. -> BackTracking (재귀 함수 사용)

answer = []

def choose(cnt):
    # N개를 다 골랐다면 출력
    if cnt == N:
        print(*answer) # 출력
        return         # 그리고 이전 함수로 돌아가서 -> 마지막 원소 제거: answer.pop() -> 다음 인덱스로 원소 추가 진행 -> ...

    # 1 ~ K까지 선택
    for i in range(1, K + 1):
        answer.append(i)      # 선택
        choose(cnt + 1)    # 다음 자리 고르기
        answer.pop()          # 선택 취소

choose(0)