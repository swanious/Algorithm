import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
mapp = [list(map(int, input().rstrip().split())) for _ in range(n)]

count_list = [[-1] * m for _ in range(n)]
sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            sy, sx = i, j
        if not mapp[i][j]:
            count_list[i][j] = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x, cnt):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] == 0:
            count_list[ny][nx] = 0

        elif 0 <= ny < n and 0 <= nx < m and count_list[ny][nx] == -1:
            q.append((ny, nx, cnt + 1))
            count_list[ny][nx] = cnt + 1

q = deque()
q.append((sy, sx, 0))
count_list[sy][sx] = 0
while q:
    v = q.popleft()
    bfs(v[0], v[1], v[2])

for i in range(n):
    print(*count_list[i])