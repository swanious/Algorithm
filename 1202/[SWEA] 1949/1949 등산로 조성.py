from collections import deque
import sys

sys.stdin = open('input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, skill, count):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if mapp[ny][nx] < mapp[y][x]:
                visited[ny][nx] = True
                q.append((ny, nx, skill, count + 1))
            elif mapp[ny][nx] == mapp[y][x]:
                if skill == 0:
                    continue
                else:
                    tmp_skill = skill
                    for k in range(1, skill + 1):
                        tmp_skill = skill - k
                        mapp[ny][nx] = mapp[ny][nx] - k
                        visited[ny][nx] = True
                        q.append((ny, nx, tmp_skill, count + 1))

            elif mapp[ny][nx] > mapp[y][x]:
                if skill == 0:
                    continue
                else:
                    tmp_skill = skill
                    for k in range(skill, -1, -1):
                        if mapp[y][x] <= mapp[ny][nx] - k:
                            continue
                        else:
                            mapp[ny][nx] = mapp[ny][nx] - k
                            visited[ny][nx] = True
                            tmp_skill = skill - k
                            q.append((ny, nx, tmp_skill, count + 1))




T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    # 봉우리 찾기
    maxV = 0
    for i in range(N):
        for j in range(N):
            if mapp[i][j] > maxV:
                maxV = mapp[i][j]

    # 봉우리 좌표 찾기
    st_arr = []
    top_cnt = 0
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == maxV:
                top_cnt += 1
                st_arr.append((i, j, K, 1))

    # bfs
    q = deque()
    cnt_arr = [0] * top_cnt
    for idx in range(len(st_arr)):
        q.append(st_arr[idx])
        visited = [[False] * N for _ in range(N)]
        while q:
            sy, sx, sk, c = q.popleft()
            visited[sy][sx] = True
            if cnt_arr[idx] <= c:
                cnt_arr[idx] = c
            bfs(sy, sx, sk, c)
    print(cnt_arr)
