from collections import deque
import sys


input = sys.stdin.readline

k = int(input())
W, H = map(int, input().split())

mapp = [list(map(int, input().split())) for _ in range(H)]
visit = [[-1] * W for _ in range(H)]
visit[0][0] = k

# 4방향
fy = [-1, 1, 0, 0]
fx = [0, 0, -1, 1]

# 8방향
ey = [-1, -2, -2, -1, 1, 2, 1, 2]
ex = [2, 1, -1, -2, -2, -1, 2, 1]


def bfs(y, x, skill, count):
    for i in range(4):
        ny = y + fy[i]
        nx = x + fx[i]
        if ny < 0 or ny >= H or nx < 0 or nx >= W or mapp[ny][nx]:
            continue
        if visit[ny][nx] < skill:
            q.append((ny, nx, skill, count + 1))
            visit[ny][nx] = skill

    if skill:
        for i in range(8):
            ny = y + ey[i]
            nx = x + ex[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W or mapp[ny][nx]:
                continue
            if visit[ny][nx] < skill - 1:
                q.append((ny, nx, skill - 1, count + 1))
                visit[ny][nx] = skill - 1


q = deque()
q.append((0, 0, k, 0))

result = -1
while q:
    v = q.popleft()
    if v[0] == H - 1 and v[1] == W - 1:
        result = v[3]
        break

    bfs(v[0], v[1], v[2], v[3])

print(result)
