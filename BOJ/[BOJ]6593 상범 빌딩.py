from collections import deque

# 층, 행, 열 체크를 위한 방향
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def escape(floor, y, x, count):
    global ans

    for di in range(6):
        nz = floor + dz[di]
        ny = y + dy[di]
        nx = x + dx[di]

        # 제한 조건 체크
        if nz < 0 or nz >= l or ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        # 벽 및 같던 곳인지 체크
        if bld[nz][ny][nx] == '#' or bld[nz][ny][nx] == 'S':
            continue

        if bld[nz][ny][nx] == '.':
            bld[nz][ny][nx] = 'S'
            q.append((nz, ny, nx, count + 1))

        # return 해주는 자리가 중요하다.
        # 모든 상황을 돌아보고 목표를 찾으면 그 때 return을 해주어야 한다.
        if bld[nz][ny][nx] == 'E':
            ans = count + 1
            return


while True:
    # 층 수, 한 층의 행, 한 층의 열
    l, n, m = map(int, input().split())
    if l == 0 and n == 0 and m == 0:
        break

    # 배열 받기(공백은 input()을 통해 날려주기)
    bld = []
    for i in range(l):
        temp_n = []
        for j in range(n):
            string = input()
            temp_m = []
            for k in string:
                temp_m.append(k)
            temp_n.append(temp_m)
        input()
        bld.append(temp_n)

    # 내 초기 위치
    q = deque()
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if bld[i][j][k] == 'S':
                    q.append((i, j, k, 0))

    ans = 0
    while q:
        v = q.popleft()
        escape(v[0], v[1], v[2], v[3])
        if ans != 0:
            break

    if ans:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')
