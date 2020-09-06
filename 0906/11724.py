'''
6 5
1 2
2 5
5 1
3 4
4 6

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''


def bfs(v):
    stack = []
    q = [v]
    visited[v] = 1
    # print(v, end=' ')
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
                # print(w, end=' ')
                stack.append(w)
    return stack


# 정점, 간선의 개수
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
cnt = 0
for i in range(E):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

for i in range(1, V + 1):
    if len(bfs(i)) >= 1 or len(G[i]) < 1:
        cnt += 1
print(cnt)