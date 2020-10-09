'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''
from collections import deque

X, Y, Z = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(Z)]

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(z, y, x, n):
    global q, max_day
    # 6방향 체크
    for i in range(6):
        ny = y + dy[i]
        nx = x + dx[i]
        nz = z + dz[i]

        # 벽 만나면 돌기
        if ny < 0 or ny >= Y or nx < 0 or nx >= X or nz < 0 or nz >= Z:
            continue

        # -1을 만나면 continue
        if arr[nz][ny][nx] == -1:
            continue

        # 값이 0이면, q에 좌표 넣기 / 익혀주기 / max_day값 올려주기
        if arr[nz][ny][nx] == 0:
            arr[nz][ny][nx] = 1
            max_day = n + 1
            q.append((nz, ny, nx, n + 1))


# 좌표 뽑기
q = deque()
day = 0
max_day = 0
for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if arr[i][j][k] == 1:
                q.append((i, j, k, day))

# q로 구현 => q.pop(0)
while len(q) != 0:
    q_list = q.popleft()
    bfs(q_list[0], q_list[1], q_list[2], q_list[3])

for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if arr[i][j][k] == 0:
                max_day = -1
print(max_day)
