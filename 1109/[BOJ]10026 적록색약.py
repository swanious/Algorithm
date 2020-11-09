'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(arr, a, b, check):
    q = deque()
    q.append((a, b))
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == check:
                q.append((ny, nx))
                arr[ny][nx] = 0

n = int(input())
mapp1 = [list(input()) for _ in range(n)]
mapp2 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mapp1[i][j] == 'R' or mapp1[i][j] == 'G':
            mapp2[i][j] = 1
        else:
            mapp2[i][j] = 2

ans1 = 0
ans2 = 0
for i in range(n):
    for j in range(n):
        if mapp1[i][j] != 0:
            bfs(mapp1, i, j, mapp1[i][j])
            ans1 += 1
        if mapp2[i][j] != 0:
            bfs(mapp2, i, j, mapp2[i][j])
            ans2 += 1
print(ans1, ans2)
