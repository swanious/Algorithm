from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0))
visit[0][0] = 1
while q:
    v = q.popleft()

    for i in range(4):
        ny = v[0] + dy[i]
        nx = v[1] + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or visit[ny][nx] != 0:
            continue

        if arr[ny][nx] == 0:
            continue

        q.append((ny, nx))
        visit[ny][nx] = visit[v[0]][v[1]] + 1

print(visit[n-1][m-1])
