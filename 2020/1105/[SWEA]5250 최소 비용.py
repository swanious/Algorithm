'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def min_cost(x, y):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            # 갈 곳의 높이 - 현재의 높이와 0 중 높은 값 + 1 ==> 거리
            dis = max(arr[ny][nx] - arr[y][x], 0) + 1
            # 갈 곳의 visit배열 값(현재 99999)가 현재의 visit배열 값 + 거리의 값보다 크면
            # -> q에 갈 곳의 y, x좌표 저장 / 갈 곳을 거리만큼 더해줌
            if visited[ny][nx] > visited[y][x] + dis:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + dis


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[99999] * N for _ in range(N)]
    visited[0][0] = 0

    q = deque()
    q.append((0, 0))
    while q:
        v = q.popleft()
        min_cost(v[0], v[1])
    print("#{} {}".format(tc, visited[N - 1][N - 1]))  # 마지막 좌표의 거리 출력
