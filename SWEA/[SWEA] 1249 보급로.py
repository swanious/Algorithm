import sys; sys.stdin = open('input.txt')

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if G[ny][nx] > G[y][x] + arr[ny][nx]:
                G[ny][nx] = G[y][x] + arr[ny][nx]
                q.append((ny, nx))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    G = [[999999] * n for _ in range(n)]
    G[0][0] = 0

    q = deque()
    q.append((0, 0))
    while q:
        v = q.popleft()
        bfs(v[0], v[1])
    print("#{} {}".format(tc, G[n-1][n-1]))