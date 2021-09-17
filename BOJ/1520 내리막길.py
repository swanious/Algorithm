import sys

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x):
    if y == 0 and x == 0:
        return 1
    if visit[y][x] == -1:
        visit[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if Matrix[ny][nx] > Matrix[y][x]:
                    visit[y][x] += dfs(ny, nx)

    return visit[y][x]

n, m = map(int, input().split())
Matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]

print(dfs(n-1, m-1))
