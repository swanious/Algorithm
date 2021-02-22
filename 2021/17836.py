from collections import deque

n, m, t = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque()
distance = 9999999

queue.append((0, 0, 0))
visited[0][0] = True


def bfs(y, x, cnt):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] != 1 and not visited[ny][nx]:
            queue.append((ny, nx, cnt + 1))
            visited[ny][nx] = True


while queue:
    v = queue.popleft()
    if mapp[v[0]][v[1]] == 2:
        distance = min(distance, v[2] + abs(v[0] - (n - 1)) + abs(v[1] - (m - 1)))

    if v[0] == n - 1 and v[1] == m - 1:
        distance = min(distance, v[2])
        break

    bfs(v[0], v[1], v[2])

if distance == 9999999 or distance > t:
    print("Fail")
else:
    print(distance)