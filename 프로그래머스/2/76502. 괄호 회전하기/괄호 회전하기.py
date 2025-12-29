def solution(s):
    answer = 0
    n = len(s)
    # s를 i칸 만큼 왼쪽으로 회전했을 때, 올바른 괄호인지 파악하는 반복문 구현
    for i in range(n):
        stack = []
        
        for j in range(n):
            c = s[(i+j)%n]
            # 열린 괄호가 나오면, 스택에 추가
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack: # 짝이 맞지 않는 경우 예외 처리
                    break
            
                # 닫힌 괄호가 나오면, 스택의 top과 짝이 맞는 지 비교
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else: # 그 외의 상황은 짝이 맞지 않는 경우로 예외 처리
                    break
        
        # break문에 의해 끝나지 않고, 끝까지 검사한 결과 answer 값 증가
        else:
            if not stack: # 짝이 모두 맞아서 스택이 비어 있는지 확인 후 예외 처리
                answer += 1
            
    return answer