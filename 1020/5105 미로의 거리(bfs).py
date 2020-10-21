from collections import deque
from pprint import pprint
import sys

sys.stdin = open('sample_input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    q = deque()
    visited = [[0] * n for _ in range(n)]
    result = 0
    ey, ex = 0, 0

    # 시작, 도착 지점 좌표 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))
            elif arr[i][j] == 3:
                ey, ex = i, j


    def bfs(y, x):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 벽 체크
            if ny < 0 or ny >= n or nx < 0 or nx >= n or arr[ny][nx] == 1:
                continue
            # 방문 체크
            if visited[ny][nx] != 0:
                continue
            if arr[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1


    # bfs 돌려주기
    while q:
        v = q.popleft()
        bfs(v[0], v[1])

    # 도착 지점 주변 숫자체크 후, 값이 존재하면 저장
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if visited[ny][nx] != 0:
            result = visited[ny][nx] - 1

    print(result)
