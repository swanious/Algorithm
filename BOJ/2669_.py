'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''

arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1 + 1, y2 + 1):
        for j in range(x1 + 1, x2 + 1):
            arr[i][j] = 1

    cnt = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == 1:
                cnt += 1

print(cnt)
