from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))

ans = 0
low, high = 0, 1
tmp = arr[low]
while low < n:
    if high == n and tmp < m:
        break

    if tmp == m:
        ans += 1
        tmp -= arr[low]
        low += 1

    elif tmp < m:
        tmp += arr[high]
        high += 1

    elif tmp > m:
        tmp -= arr[low]
        low += 1
print(ans)