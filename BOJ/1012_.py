import sys

# 재귀 한도를 5000으로 만들어주지 않으면 런타임에러 발생!!
sys.setrecursionlimit(5000)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    # 배추를 지워준다.(왔던 곳은 가지 않도록 visit 체크)
    ground[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 다음 장소에 배추가 있으면 dfs
        if 0 <= ny < n and 0 <= nx < m and ground[ny][nx]:
            dfs(ny, nx)


round = int(input())
for _ in range(round):

    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    bugs = 0

    # 배추의 위치를 받아온다.
    for _ in range(k):
        a, b = map(int, input().split())
        ground[b][a] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                dfs(i, j)
                bugs += 1

    print(bugs)