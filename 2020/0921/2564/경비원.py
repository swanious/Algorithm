'''
10 5
3
1 4
3 2
2 8
2 3
'''
w, h = map(int, input().split())
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
X = list(map(int, input().split()))

result = 0

for i in range(n):
    if arr[i][0] == X[0]:
        result += abs(arr[i][1] - X[1])
    # X의 위치가 북쪽일때
    elif X[0] == 1:
        if arr[i][0] == 2:
            a = X[1] + arr[i][1] + h
            b = (w - X[1]) + (w - arr[i][1]) + h
            result += min(a, b)
        elif arr[i][0] == 3:
            result += X[1] + arr[i][1]
        elif arr[i][0] == 4:
            result += (w - X[1]) + arr[i][1]

    elif X[0] == 2:
        if arr[i][0] == 1:
            a = X[1] + arr[i][1] + h
            b = (w - X[1]) + (w - arr[i][1]) + h
            result += min(a, b)
        elif arr[i][0] == 3:
            result += X[1] + (h-arr[i][1])
        elif arr[i][0] == 4:
            result += (w - X[1]) + (h - arr[i][1])

    elif X[0] == 3:
        if arr[i][0] == 4:
            a = X[1] + arr[i][1] + w
            b = (h - X[1]) + (h - arr[i][1]) + w
            result += min(a, b)
        elif arr[i][0] == 1:
            result += X[1] + arr[i][1]
        elif arr[i][0] == 2:
            result += (h - X[1]) + arr[i][1]

    elif X[0] == 4:
        if arr[i][0] == 3:
            a = X[1] + arr[i][1] + w
            b = (h - X[1]) + (h - arr[i][1]) + w
            result += min(a, b)
        elif arr[i][0] == 1:
            result += X[1] + (w - arr[i][1])
        elif arr[i][0] == 2:
            result += (h - X[1]) + (w - arr[i][1])

print(result)
