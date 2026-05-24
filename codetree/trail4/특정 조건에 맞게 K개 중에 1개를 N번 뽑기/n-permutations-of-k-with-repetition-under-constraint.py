K, N = map(int, input().split())

# Please write your code here.

arr = []

def choose(cnt):
    
    if cnt == N:
        print(*arr)
        return
    
    for i in range(1,K+1):
        # 연속하여 같은 숫자가 3번 나오는 경우는 제외
        if cnt >= 2 and arr[-1] == arr[-2] == i:
            continue

        # 백트래킹으로 모든 순서쌍 뽑기
        arr.append(i)
        choose(cnt + 1)
        arr.pop()

choose(0)