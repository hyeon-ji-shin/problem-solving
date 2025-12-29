DIRS = ['U', 'D', 'L', 'R']
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
    
# 좌표평면을 벗어나지 않는 범위 파악하는 함수
def is_valid(nx, ny):
    return 0<=nx<11 and 0<=ny<11

def move(x, y, dir):    
    idx = DIRS.index(dir)
    nx = x + DX[idx]
    ny = y + DY[idx]
    
    return nx, ny
    
def solution(dirs):
    x,y = 5, 5 # 현재 위치 (x, y) 표현
    ans = set() # 같은 길을 갔더라도 중복되지 않도록 set 사용
    for dir in dirs:
        nx, ny = move(x, y, dir)
        if not is_valid(nx, ny): # 범위를 벗어나는 좌표는 무시
            continue

        ans.add((x,y,nx,ny)) # 방향 무시를 위해 양방향 추가
        ans.add((nx,ny,x,y))
        x, y = nx, ny
    
    answer = len(ans)/2 # 방향 무시를 위해 1/2
    return answer