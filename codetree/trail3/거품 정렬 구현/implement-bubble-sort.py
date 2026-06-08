n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

sorted_flag = False

while not sorted_flag:
    sorted_flag=True
    for i in range (n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
            sorted_flag=False

print(*arr)