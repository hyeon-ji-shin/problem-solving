n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = 0
for i in range (n-2):
    for j in range (n-2):
        cnt = 0
        
        for x in range(i,i+3):
            for y in range(j,j+3):
                cnt += grid[x][y]
        
        ans = max(ans, cnt)

print(ans)