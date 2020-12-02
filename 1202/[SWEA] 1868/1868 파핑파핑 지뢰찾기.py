import sys;

sys.stdin = open('input.txt')

import collections

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(y, x):
    q = collections.deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        cur_y, cur_x = q.popleft()
        for i in range(8):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                if mapp[ny][nx] == 0:  # 연쇄적으로 클릭할 수 있으면 클릭
                    q.append((ny, nx))


def mine_check(y, x):
    cnt = 0

    for i in range(8):
        ny = y + dy[i]
        nx = x  + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if mapp[ny][nx] == '*':
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    mapp = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

    zero_list = []
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == '.':
                mapp[i][j] = mine_check(i, j)

            if mapp[i][j] == 0:
                zero_list.append((i, j))

    print(mapp)
    ans = 0
    visited = [[False] * n for _ in range(n)]

    for y, x in zero_list:
        if visited[y][x]: continue
        bfs(y, x)
        ans += 1

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and mapp[i][j] != '*':
                ans += 1
    print("#{} {}".format(tc, ans))
