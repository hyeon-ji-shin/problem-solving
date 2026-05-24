n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 각 위치의 폭탄 여부 및 종류 표현할 배열.
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
# 폭발 영역 표시할 배열.
bombed = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0
bomb_pos = list() #폭탄 설치 위치 저장

# 격자 내 위치 여부 판단 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 주어진 폭탄 정보에 따라, 폭발 영역 표시하는 함수
def bomb(x, y, b_type):
    # 폭탄 종류에 따른 폭발 범위 사전 정의.
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]
    # grid 내 칸에 대해서만 폭발 영역 표시하기
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i]
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed[nx][ny] = True

# 현재 배치에서 폭발 영역 계산하기
def calc():
    # 폭발 여부 배열 초기화
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False
    
    # 각 폭탄에 대하여, 폭탄 유형이 정의되어있다면, 그에 따른 폭발 영역 표시
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])
    
    # 폭발 영역 cnt
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1
    return cnt

# 폭탄 종류에 따른 폭발 가능 영역 모두 탐색 (백트래킹)
# cnt번째의 폭탄 종류 결정
def find_max_area(cnt):
    global ans
    # 모든 폭탄의 종류 결정했다면
    if cnt == len(bomb_pos): 
        ans = max(ans, calc()) # 현재 조합의 폭발 영역 계산
        return
    
    # 현재 폭탄의 위치에 대해서 종류 1~3 모두 시도
    for i in range(1, 4):
        x, y = bomb_pos[cnt] # 폭탄 위치 불러오기
        bomb_type[x][y] = i
        find_max_area(cnt + 1) # 다음 폭탄 결정 (재귀)
        bomb_type[x][y] = 0 # 다음 경우의 수 탐색을 위해

# 폭탄 위치 저장
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            bomb_pos.append((i, j))


find_max_area(0)

print(ans)