from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
print(G)


def bfs(num, cnt):
    for w in G[num]:
        print(w)
        if not visit[w]:
            q.append((w, cnt + 1))
            visit[w] = True
            result[w] += 1


visit = [False] * (n + 1)
result = [0] * (n + 1)
for i in range(1, n + 1):
    q = deque()
    visit[i] = True
    q.append((i, 0))
    while q:
        v = q.popleft()
        bfs(v[0], v[1])
    print(result)
    print(sum(result))
