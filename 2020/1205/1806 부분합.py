'''
10 15
5 1 3 5 10 7 4 9 2 8
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

low, high = 0, 1
tmp = arr[low]
ans = 0
while low < n:
    if high == n and tmp < m:
        break

    if tmp >= m:
        if ans == 0:
            ans = high - low
        elif ans > (high - low):
            ans = high - low
        tmp -= arr[low]
        low += 1

    elif tmp < m:
        tmp += arr[high]
        high += 1


print(ans)
