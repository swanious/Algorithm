'''
5 5 2 2 3
2 2
3 2
3 3
4 1
1 4
'''
from collections import deque
from pprint import pprint

n, m, a, b, k = map(int, input().split())
mapp = [[0] * (m + 1) for _ in range(n + 1)]

# 가장자리 벽만들기
for i in range(n + 1):
    mapp[i][0] = 1
for i in range(m + 1):
    mapp[0][i] = 1

# 장애물 좌표 지정
for i in range(k):
    temp1, temp2 = map(int, input().split())
    mapp[temp1][temp2] = 1

sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

q = deque()
# 시작 위치 지정
for i in range(sy, sy + a):
    for j in range(sx, sx + b):
        mapp[i][j] = 2
        q.append((i, j, 0))

print(q)
# 종료 위치 지정
for i in range(ey, ey + a):
    for j in range(ex, ex + b):
        mapp[i][j] = 3

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

cnt = 0


def bfs(y, x, count):
    global cnt

    k_cnt = [0] * 4
    for i in range(y, y + a):
        for j in range(x, x + b):
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or ny > n or nx < 0 or nx > m:
                    continue
                if mapp[ny][nx] == 1:
                    continue
                k_cnt[k] += 1

    flag = False
    for i in range(4):
        if k_cnt[i] == a * b:
            flag = True
            mapp[y + dy[i]][x + dx[i]] = 2
            q.append((y + dy[i], x + dx[i], count + 1))
    if flag == False:
        cnt = -1
    k_cnt = [0] * 4


while q:
    v = q.popleft()
    if v[0] == ey and v[1] == ex:
        cnt = v[2]
        break
    bfs(v[0], v[1], v[2])

pprint(mapp)
print(cnt)
