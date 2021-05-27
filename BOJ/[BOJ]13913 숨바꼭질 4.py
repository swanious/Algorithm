from collections import deque


def bfs(x):
    y = x - 1
    if 0 <= y <= MAX and visited[y] == -1:
        visited[y] = x
        q.append(y)

    y = x + 1
    if 0 <= y <= MAX and visited[y] == -1:
        visited[y] = x
        q.append(y)

    y = x * 2
    if 0 <= y <= MAX and visited[y] == -1:
        visited[y] = x
        q.append(y)


a, b = map(int, input().split())
MAX = max(a, b) + 1
visited = [-1] * (MAX + 1)

# bfs
q = deque()
q.append(a)
while q:
    v = q.popleft()
    if v == b:
        break
    bfs(v)

# 답 찾기
parent = []
while b != a:
    parent.append(b)
    b = visited[b]

parent.append(a)  # 리스트에 첫 숫자 넣고 reverse(거꾸로 찾아가므로)
parent = list(reversed(parent))
print(len(parent)-1)
print(*parent)