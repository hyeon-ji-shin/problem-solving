def solution(s):
    
    stack = []
    
    for c in s:
        # 스택이 비어 있지 않고, 현재 문자와 스택의 맨 위 문자가 같으면
        if stack and stack[-1] == c:
            # 스택의 맨 위 문자 제거
            stack.pop()
        else:
            # 아니면, 스택에 현재 문자 추가
            stack.append(c)
    # 스택이 비어 있으면 1, 아니면 0 반환
    return int(not stack)