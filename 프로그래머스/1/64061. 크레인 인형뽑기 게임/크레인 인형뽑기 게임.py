def solution(board, moves):
    # N x N 크기의 배열 board에서의 각 열에 대한 스택을 생성
    stacks = [[] for _ in range(len(board[0]))]
    
    # 배열 board를 역순으로 탐색하여 각 열의 인형을 stacks에 추가
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                stacks[j].append(board[i][j])
    
    # 인형을 담을 바구니 생성
    basket = [ ]
    answer = 0

    for m in moves:
        if stacks[m-1]: # 해당 열에 인형이 있는 경우
            temp = stacks[m-1].pop()
            if basket and basket[-1] == temp: # 바구니에 인형이 있고, 바구니 가장 위에 있는 인형과 같은 경우
                basket.pop()
                answer += 2
            else:
                basket.append(temp)
    return answer