from collections import deque


n, m = map(int, input().split())
link = [[] for _ in range(n + 1)]
link_num = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link_num[b] += 1

q = deque()
for i in range(1, n + 1):
    if not link_num[i]:
        q.append(i)

while q:
    num = q.popleft()
    print(num, end=' ')
    for i in link[num]:
        link_num[i] -= 1
        if not link_num[i]:
            q.append(i)
