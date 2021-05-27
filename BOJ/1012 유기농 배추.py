import sys

sys.setrecursionlimit(50000)
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    global tmp

    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if G[ny][nx] and not visited[ny][nx]:
                tmp += 1
                dfs(ny, nx)


for tc in range(int(input())):
    m, n, k = map(int, input().split())

    visited = [[False] * m for _ in range(n)]
    G = [[0] * m for _ in range(n)]
    baechu = []

    tmp = 0
    for _ in range(k):
        x, y = map(int, input().split())
        baechu.append((x, y))
        G[y][x] = 1

    for x, y in baechu:
        dfs(y, x)

    print(k - tmp)
