'''
3 3
D.*
...
.S.
'''
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

ey, ex, sy, sx = 0, 0, 0, 0
star = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D':
            ey, ex = i, j
        if arr[i][j] == 'S':
            sy, sx = i, j
        if arr[i][j] == '*':
            star.append((i, j))


def bfs(y, x):
    # y,x가 고슴도치 위치였을 경우
    if arr[y][x] == 'S':
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if arr[ny][nx] == 'X' or arr[ny][nx] == '*':
                continue

            if arr[ny][nx] == '.':
                arr[ny][nx] = 'S'

    # y,x가 물 위치였을 경우
    elif arr[y][x] == '*':
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if arr[ny][nx] == 'X' or arr[ny][nx] == 'S':
                continue

            if arr[ny][nx] == '.':
                arr[ny][nx] = '*'
