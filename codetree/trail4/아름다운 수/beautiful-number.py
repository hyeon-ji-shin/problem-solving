# 변수 선언 및 입력:
n = int(input())
ans = 0
seq = list()


def is_beautiful():
    i = 0 # 연달아 같은 숫자가 나오는 지 파악할 시작 위치
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면 아름다운 수 X
        if i + seq[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자 seq[i]만큼 같은 숫자가 있는지 확인.
        # 하나라도 다른 숫자가 있다면, 아름다운 수 X
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
        # i에서 (i+seq[i]-1)까지 같은 숫자가 있는 걸 확인했으므로, 다음 i+seq[i]부터 연속 숫자 이어서 확인.
        i += seq[i] 
        
    return True


def count_beautiful_seq(cnt):
    global ans
    
    # 만들어진 seq가 원하는 N자리 수가 되었을 때, seq가 아름다운 수인지 확인
    if cnt == n:
        if is_beautiful():
            ans += 1
        return
    
    # (재귀 활용) 1 ~ 4 사이의 숫자로 이루어진 수열 만들기
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(0)
print(ans)
