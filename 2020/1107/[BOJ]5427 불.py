'''
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
'''

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, count):
    global ans

    # 상근이 시점
    if mapp[y][x] == '@':
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            # 현재 좌표가 나갈 수 있는 경우면 탈출
            if y == n - 1 or y == 0 or x == m - 1 or x == 0:
                ans = count + 1
                return

            # 벽, 불이면 skip
            if 0 > ny or ny >= n or 0 > nx or nx >= m or mapp[ny][nx] == '#' or mapp[ny][nx] == '*':
                continue

            # 벽이 아니고, 갈 수 있으면 대피
            if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] == '.':
                mapp[ny][nx] = '@'
                q.append((ny, nx, count + 1))

    # 불 시점
    elif mapp[y][x] == '*':
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            # 벽, 상근이면 skip
            if 0 > ny or ny >= n or 0 > nx or nx >= m or mapp[ny][nx] == '#' or mapp[ny][nx] == '@':
                continue

            # 벽이 아니고 갈 수 있으면 점화
            if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] == '.':
                mapp[ny][nx] = '*'
                q.append((ny, nx, count))


T = int(input())
for tc in range(1, T + 1):
    m, n = map(int, input().split())
    mapp = [list(input()) for _ in range(n)]

    sY, sX = 0, 0
    fire = []  # 불 좌표를 담을 리스트
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == '@':  # 상근이의 좌표
                sY, sX = i, j

            if mapp[i][j] == '*':  # 불의 좌표들
                fire.append((i, j, 0))

    ans = 0
    q = deque()
    for i in fire:  # 불
        q.append(i)
    q.append((sY, sX, 0))  # 상근

    while q:
        v = q.popleft()
        bfs(v[0], v[1], v[2])
        if ans != 0:
            break

    if ans == 0:
        print('IMPOSSIBLE')
    else:
        print(ans)
