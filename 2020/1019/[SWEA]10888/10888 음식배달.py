import sys
from itertools import combinations
from collections import deque

sys.stdin = open('sampleinput.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    store = []
    q = deque()

    # 4방향 설정
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    combi = []


    def bfs(y, x):
        global result

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx] >= 0:
                continue
            visited[ny][nx] = visited[y][x] + 1
            if arr[ny][nx] == 1:
                result += visited[ny][nx]

            q.append((ny, nx))


    # 조합 구하기
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                store.append((i, j))

    if len(store) > 0:
        for i in range(1, len(store) + 1):
            a = combinations(store, i)
            combi += a

    result_list = []
    for i in combi:
        result = 0
        visited = [[-1] * n for _ in range(n)]
        for j in range(len(i)):
            result += arr[i[j][0]][i[j][1]]  # 초기 상점의 값
            visited[i[j][0]][i[j][1]] = 0
            q.append(i[j])

        while q:
            v = q.popleft()
            bfs(v[0], v[1])
        result_list.append(result)

    print(f'#{tc} {min(result_list)}')