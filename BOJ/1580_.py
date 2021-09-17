from collections import deque

n, m = map(int, input().split())
mapp = [list(input()) for _ in range(n)]
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

A, B = [], []
q = deque()
result = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'X':
            mapp[i][j] = -1
        elif mapp[i][j] == 'A':
            A = [i, j]
        elif mapp[i][j] == 'B':
            B = [i, j]
        else:
            mapp[i][j] = 0

visit[A[0]][A[1]][B[0]][B[1]] = True

dy = [0, 1, 1, 1, 0, 0, -1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 0, 1, -1]

def bfs(ay, ax, by, bx, cnt):
    global result

    for i in range(9):
        for j in range(9):
            nay = ay + dy[i]
            nax = ax + dx[i]
            nby = by + dy[j]
            nbx = bx + dx[j]

            # 범위 체크
            if 0 > nay or nay >= n or 0 > nax or nax >= m:
                continue
            if 0 > nby or nby >= n or 0 > nbx or nbx >= m:
                continue

            # 충돌 방지턱
            if nay == nby and nax == nbx:
                continue
            # 크로스 금지령
            if ay == nby and ax == nbx and by == nay and bx == nax:
                continue

            # 벽에 머리박기 금지
            if mapp[nay][nax] == -1 or mapp[nby][nbx] == -1:
                continue

            if not visit[nay][nax][nby][nbx]:
                q.append((nay, nax, nby, nbx, cnt + 1))
                visit[nay][nax][nby][nbx] = True



q.append((A[0], A[1], B[0], B[1], 0))
while q:
    v = q.popleft()
    if v[0] == B[0] and v[1] == B[1] and v[2] == A[0] and v[3] == A[1]:
        result = v[4]
        break
    bfs(v[0], v[1], v[2], v[3], v[4])

if result == 0:
    print(-1)
else:
    print(result)