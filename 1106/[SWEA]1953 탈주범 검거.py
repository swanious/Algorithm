from collections import deque


# 파이프 호환 유효성 검사(갈 수 있는 d 체크)
valid = {1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]}

# 각 방향별로 갈 수 있는 곳 체크
check = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]

# 방향
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(x, y, cnt):
    global result

    for i in valid[arr[y][x]]:
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            if arr[ny][nx] in check[i]:
                q.append((nx, ny, cnt + 1))
                visited[ny][nx] = True


T = int(input())
for tc in range(1, T + 1):
    n, m, c, r, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    stY, stX = c, r
    visited[stY][stX] = True

    result = 0
    q = deque()
    q.append((stX, stY, 0))
    while q:
        v = q.popleft()
        if v[2] == time - 1:  # 시간 제한
            break
        bfs(v[0], v[1], v[2])


    for i in range(n):
        for j in range(m):
            if visited[i][j] == True:
                result += 1
    print("#{} {}".format(tc, result))