n = int(input())
arr = list(input())
cnt = 0
if arr[0] == 'W':
    cnt += 1
elif arr[-1] == 'E':
    cnt += 1

for i in range