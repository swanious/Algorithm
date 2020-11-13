from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if mapp[ny][nx] == 0:
                visited[ny][nx] = -1
                q.append((ny, nx))
        if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] == 1:
            visited[ny][nx] = visited[ny][nx] + 1

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    while q:
        v = q.popleft()
        bfs(v[0], v[1])

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                mapp[i][j] = 0
    ans += 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                cnt += 1
    if cnt == (n * m):
        break
print(ans)