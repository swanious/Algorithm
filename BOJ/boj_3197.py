from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split(' '))
mapp = [list(input().strip()) for _ in range(n)]
ey, ex = 0, 0
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
w_visit = [[False] * m for _ in range(n)]
s_visit = [[False] * m for _ in range(n)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()
ans = 0

def water():
    while wq1:
        y, x = wq1.popleft()
        mapp[y][x] = '.' # change ice to water
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m or w_visit[ny][nx]: continue
            if mapp[ny][nx] == '.':
                wq1.append((ny, nx))
            else:
                wq2.append((ny, nx))
            w_visit[ny][nx] = True

def swan():
    while sq1:
        y, x = sq1.popleft()
        # swan fall in love
        if y == ey and x == ex:
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m or s_visit[ny][nx]: continue
            if mapp[ny][nx] == '.': # you can go, swan
                sq1.append((ny, nx))
            else:
                sq2.append((ny, nx)) # you can't..
            s_visit[ny][nx] = True
    return False

for i in range(n):
    for j in range(m):
        # 백조
        if mapp[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                s_visit[i][j] = True
            else:
                ey, ex = i, j
            mapp[i][j] = '.'
        # 워으터
        if mapp[i][j] == '.':
            wq1.append((i, j))
            w_visit[i][j] = True
while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1

print(ans)