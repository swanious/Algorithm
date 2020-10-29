'''
3 6
D...*.
.X.X..
....S.

5 4
.D.*
....
..X.
S.*.
....

'''
from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

sy, sx, ey, ex = 0, 0, 0, 0
flood = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


# 시작, 도착, 물의 위치 저장
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D':
            ey, ex = i, j
        if arr[i][j] == 'S':
            sy, sx = i, j
        if arr[i][j] == '*':
            flood.append((i, j))

visit = [[0] * m for _ in range(n)]
cnt_S = 0
flag = False

def bfs(y, x):
    global cnt_S, flag

    # pop한게 고슴도치일 때
    if arr[y][x] == 'S':

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:  # 벽 체크
                continue
            if arr[ny][nx] == '*' or arr[ny][nx] == 'X':  # 물이거나, 벽이면 스킵
                continue

            # 4방 체크에서 '.'이 2개 이상일 수도 있으므로
            if arr[ny][nx] == '.':
                arr[ny][nx] = 'S'
                visit[ny][nx] = visit[y][x] + 1
                q.append((ny, nx))

            if arr[ny][nx] == 'D':
                visit[ny][nx] = visit[y][x] + 1
                flag = True
                break

    # pop한 것이 물일 때
    elif arr[y][x] == '*':
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:  # 벽 체크
                continue
            if arr[ny][nx] == '.':
                arr[ny][nx] = '*'
                q.append((ny, nx))


# 큐에 물 / 고슴도치의 좌표를 받아줌
q = deque()
for i in range(len(flood)):
    q.append(flood[i])
q.append((sy, sx))

while q:
    if flag == True:
        break
    v = q.popleft()
    bfs(v[0], v[1])


if visit[ey][ex] == 0:
    print('KAKTUS')
else:
    print(visit[ey][ex])
