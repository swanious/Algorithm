'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
'''
from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 초기 좌표
y, x = 0, 0
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            y, x = i, j
            q.append((y, x, 0)) # 1이 한 개 이상 존재할 수도 있으므로 q에 미리넣고 시작한다.

cnt = 0
# 4방향 지정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, count):
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if arr[ny][nx] == -1:
            continue

        if arr[ny][nx] == 0:
            arr[ny][nx] = 1
            cnt = count + 1
            q.append((ny, nx, count + 1))


while q:
    bfs(*q.popleft())

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt = -1
print(cnt)