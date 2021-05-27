n = int(input())
arr = list(map(int, input().split()))
s = int(input())

max_int, idx = -999, 0
large_int = []
cnt = s
while cnt:
    for i in range(cnt + 1):
        if i == len(arr):
            break

        if arr[i] > max_int:
            max_int, idx = arr[i], i

    if not len(arr):
        break

    large_int.append(arr[idx])
    arr.remove(arr[idx])
    cnt -= idx
    max_int = -999
    idx = 0

print(*(large_int + arr))