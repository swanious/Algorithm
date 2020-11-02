'''
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
'''
'''
핵심은 벽이 아닌 곳을 먼저 둘러보고(appendleft), 벽인 곳은 나중에 둘러보기(append)
+ visit배열을 잘 활용하기 !
'''
from collections import deque
from pprint import pprint
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if visited[ny][nx] == -1:
            # 벽은 후순위(append)
            if miro[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

            # 벽이 아닌 곳은 선순위(appendleft)
            if miro[ny][nx] == 1:
                visited[ny][nx] = visited[y][x]
                q.appendleft((ny, nx))


n = int(input())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
visited[0][0] = 0

q = deque()
q.append((0, 0))
while q:
    v = q.popleft()
    bfs(*v)
pprint(visited)
print(visited[n-1][n-1])
