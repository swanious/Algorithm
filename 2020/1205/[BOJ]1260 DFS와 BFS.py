V, E, st = map(int, input().split())

G = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
visited[st] = True

dfs_result = []
bfs_result = []

# 인접 리스트
for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(v):
    global dfs_result

    dfs_result.append(v)
    for w in sorted(G[v]):
        if not visited[w]:
            visited[w] = True
            dfs(w)

def bfs(v):
    global bfs_result

    q = [v]
    while q:
        node = q.pop(0)
        bfs_result.append(node)
        for w in sorted(G[node]):
            if not visited[w]:
                visited[w] = True
                q.append(w)

# dfs
dfs(st)

# visited배열 초기화 및 bfs
visited = [False] * (V + 1)
visited[st] = True
bfs(st)

print(" ".join(list(map(str, dfs_result))))
print(" ".join(list(map(str, bfs_result))))
