# 복구 기능은 stack을 사용하면 O(1).

# 배열을 만드는 방식은 삽입, 삭제 기능을 구현하는 데 연산이 오래 걸림
# -> 문제에서 반환하는 정보는 삭제 여부이므로, Linked List로 인덱스만으로 연산하는 방식을 채택.

def solution(n, k, cmd):
    # 삭제된 행의 인덱스를 저장하는 리스트
    deleted = []
    
    # Linked List에서 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    
    # 현재 위치를 나타내는 인덱스
    k += 1
    
    # 주어진 명령어(cmd) 리스트를 하나씩 처리
    for current_cmd in cmd:
        if current_cmd.startswith("C"):
            deleted.append(k)     # 삭제한 인덱스는 추후 복구를 위해 스택에 추가.
            up[down[k]] = up[k]   # 현재 선택 인덱스 k의 아래에 있는 행의 윗부분 = k의 윗부분
            down[up[k]] = down[k] # 현재 선택 인덱스 k의 윗에 있는 행의 아랫부분 = k의 아랫부분
            k = up[k] if n < down[k] else down[k] # 인덱스 삭제했으니 k 업데이트
        elif current_cmd.startswith("Z"):
            r = deleted.pop() # 가장 최근 삭제한 인덱스를 복구
            up[down[r]] = r   # 복구할 인덱스의 아래에 있는 행의 윗부분 = 복구할 인덱스 : "C" 했을 때 바뀐 값 복구
            down[up[r]] = r   # 복구할 인덱스의 위에 있는 행의 아래부분 = 복구할 인덱스 : "C" 했을 때 바뀐 값 복구
        else:
            action, num = current_cmd.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]  
    
    # 최종 결과 
    answer = ["O"]*n
    for i in deleted:
        answer[i-1] = "X" # deleted에서 사용한 인덱스는 1부터 시작하므로 i-1 반영
    return "".join(answer)