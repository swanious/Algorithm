from collections import deque

dy = [0, 0, 1, 1, 1, -1, -1, -1]
dx = [1, -1, 0, -1, 1, 0, -1, 1]

# 땅-1, 바다-0
def bfs(y, x):
    global cnt

    arr[y][x] = 0
    for z in range(8):
        ny = y + dy[z]
        nx = x + dx[z]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if arr[ny][nx] == 0:
            continue

        if visit[ny][nx]:
            continue

        if arr[ny][nx] == 1:
            q.append((ny, nx))
            visit[ny][nx] = True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    q = deque()
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (arr[i][j] == 1) and not visit[i][j]:
                visit[i][j] = True
                q.append((i, j))
                while q:
                    bfs(*q.popleft())
                cnt += 1

    print(cnt)