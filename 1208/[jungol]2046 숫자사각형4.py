n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if m == 1:
            arr[j][i] = j + 1
        elif m == 2:
            if i % 2 == 0:
                arr[i][j] = j + 1
            else:
                arr[i][n - j - 1] = j + 1
        else:
            arr[i][j] = (i + 1) * (j + 1)

for i in range(n):
    print(*arr[i])


'''
정답
4 1
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

4 2
1 2 3 4
4 3 2 1
1 2 3 4
4 3 2 1

4 3
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
'''