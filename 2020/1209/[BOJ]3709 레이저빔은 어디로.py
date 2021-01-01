# 오, 아, 왼, 위
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x, dir):
    global ans_y, ans_x

    ny = y + dy[dir]
    nx = x + dx[dir]

    # 순환구조면 0,0 반환
    if dir in visit[ny][nx]:
        ans_y, ans_x = 0, 0
        return

    # 순환구조가 아니고, 범위를 벗어나면 정답(레이저가 범위 밖으로 나가면)
    if ny == 0 or ny > n or nx == 0 or nx > n:
        ans_y, ans_x = ny, nx
        return

    # 거울을 만났을 때
    if arr[ny][nx] == -1:
        visit[ny][nx].append(dir)
        dfs(ny, nx, (dir + 1) % 4)
    else:
        dfs(ny, nx, dir)


T = int(input())
for tc in range(1, T + 1):
    n, r = map(int, input().split())
    arr = [[0] * (n + 2) for _ in range(n + 2)]
    visit = [[[] for _ in range(n+2)] for _ in range(n + 2)]

    for i in range(r):
        a, b = map(int, input().split())
        arr[a][b] = -1

    sy, sx = map(int, input().split())

    dir = 0
    if sy > n:     # y가 n보다 크면, 위
        dir = 3
    elif sy < 1:   # y가 1보다 작으면, 아래
        dir = 1
    elif sx > n:   # x가 1보다 작으면, 오른쪽
        dir = 2
    else:          # x가 n보다 크면, 왼
        dir = 0

    ans_y, ans_x = 0, 0
    dfs(sy, sx, dir)
    print(ans_y, ans_x)
