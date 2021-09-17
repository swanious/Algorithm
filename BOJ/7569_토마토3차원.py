from collections import deque

'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
dh = [1, -1]
q = deque()
zero_cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                zero_cnt += 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k, 0))

cnt = 0


def bfs(hi, y, x, count):
    global cnt

    for i in range(2):
        nh = hi + dh[i]
        if nh < 0 or nh >= h:
            continue

        if arr[nh][y][x] == -1:
            continue

        if arr[nh][y][x] == 0:
            cnt = count + 1
            q.append((nh, y, x, count + 1))
            arr[nh][y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if arr[hi][ny][nx] == -1:
            continue

        if arr[hi][ny][nx] == 0:
            cnt = count + 1
            q.append((hi, ny, nx, count + 1))
            arr[hi][ny][nx] = 1


# bfs 돌려돌려 돌림판
while q:
    bfs(*q.popleft())

# 배열에 0이 없으면 cnt는 0
if zero_cnt == 0:
    cnt = 0

# 배열에 0이 존재하면, cnt는 -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                cnt = -1
print(cnt)
