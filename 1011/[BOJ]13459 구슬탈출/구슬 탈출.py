from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

red = []
blue = []
ball_map = tuple()
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            arr[i][j] = 2

        elif arr[i][j] == 'O':
            arr[i][j] = 1

        # 초기 R의 좌표
        elif arr[i][j] == 'R':
            arr[i][j] = 0
            red.append(i)
            red.append(j)

        # 초기 B의 좌표
        elif arr[i][j] == 'B':
            arr[i][j] = 0
            blue.append(i)
            blue.append(j)

        elif arr[i][j] == '.':
            arr[i][j] = 0

# 첫 방문 체크
visited[red[0]][red[1]][blue[0]][blue[1]] = True
ball_map = (red[0], red[1], blue[0], blue[1], 0)
q = deque()
q.append(ball_map)

# 4방향 지정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(rry, rrx, bby, bbx, count):
    global result, q
    count += 1

    if count > 10:
        result = 0
        q = []
        return

    for i in range(4):
        ry = rry
        rx = rrx
        by = bby
        bx = bbx

        ry, rx = straight(ry, rx, by, bx, i)
        by, bx = straight(by, bx, ry, rx, i)
        ry, rx = straight(ry, rx, by, bx, i)

        if arr[by][bx] == 1:
            result = 0
            continue

        elif arr[ry][rx] == 1:
            result = 1
            q = []
            return

        if visited[ry][rx][by][bx]:
            continue

        visited[ry][rx][by][bx] = True
        q.append((ry, rx, by, bx, count))


def straight(moveY, moveX, stopY, stopX, dir):
    y, x = moveY, moveX
    ny = y + dy[dir]
    nx = x + dx[dir]
    while True:
        if arr[ny][nx] == 2:
            break

        elif ny == stopY and nx == stopX:
            if arr[ny][nx] == 1:
                y = ny
                x = nx
            break

        elif arr[y][x] == 1:
            break

        y = ny
        x = nx
        ny = y + dy[dir]
        nx = x + dx[dir]

    return y, x


while q:
    bfs(*q.popleft())

print(result)