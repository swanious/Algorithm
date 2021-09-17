n = int(input())
arr = list(input())
cnt = 0
if arr[0] == 'W': cnt += 1
elif arr[-1] == 'E': cnt += 1
for i in range(len(arr)-1):
    if arr[i]+arr[i+1] == 'EW': cnt += 1
print(cnt)