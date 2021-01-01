from collections import deque

dxy = [1, -1]

def bfs(y, x, dir, mirror):
    # 가로
    if dir == 1:
        for i in range(2):
            ny = y
            while True:
                ny = ny + dxy[i]
                if ny < 0 or ny >= h:
                    break
                if visited[ny][x] != 0 and visited[ny][x] != mirror + 1:
                    break
                visited[ny][x] = mirror + 1
                q.append((ny, x, 2, mirror + 1))


    # 세로
    else:
        for i in range(2):
            nx = x
            while True:
                nx = nx + dxy[i]
                if nx < 0 or nx >= w:
                    break
                if visited[y][nx] != 0 and visited[y][nx] != mirror + 1:
                    break
                visited[y][nx] = mirror + 1
                q.append((y, nx, 1, mirror + 1))


w, h = map(int, input().split())
arr = [list(input()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]

c_list = []
sy, sx, ey, ex = 0, 0, 0, 0
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            c_list.append([i, j])
        elif arr[i][j] == '*':
            visited[i][j] = -1

sy, sx = c_list[0]
ey, ex = c_list[1]

ans = 0
q = deque()
q.append((sy, sx, 1, 0))
q.append((sy, sx, 2, 0))
while q:
    v = q.popleft()
    bfs(*v)

ans = visited[ey][ex]
print(ans - 1)