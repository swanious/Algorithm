n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            arr[i][j] = num + 1
            num += 1
        else:
            arr[i][m - j - 1] = num + 1
            num += 1

for i in range(n):
    print(*arr[i])

'''
정답 형식
4 6
1 2 3 4 5 6
12 11 10 9 8 7
13 14 15 16 17 18
24 23 22 21 20 19
'''