'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''
from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
temp_list = deepcopy(arr)

# 바이러스의 위치 좌표 받을 list에 y, x 좌표를 저장
temp = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            temp.append([i, j, 0])

# 바이러스 위치 좌표에서 m만큼 뽑은 모든 조합 저장
virus_comb = list(combinations(temp, m))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, count):
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n or arr[ny][nx] == 1:
            continue

        if arr[ny][nx] == 0 or arr[ny][nx] == 2:
            if arr[ny][nx] == 0:
                cnt = count + 1
            arr[ny][nx] = 1
            q.append([ny, nx, count + 1])


cnt_list = []
# 바이러스의 갯수만큼 bfs돌기
for i in range(len(virus_comb)):
    q = deque()
    for j in range(m):
        q.append(virus_comb[i][j])
    cnt = 0
    while q:
        v = q.popleft()
        bfs(v[0], v[1], v[2])


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt = 9999999
                break

        if cnt == 9999999:
            break

    cnt_list.append(cnt)
    arr = deepcopy(temp_list)

if min(cnt_list) == 9999999:
    print(-1)
else:
    print(min(cnt_list))
