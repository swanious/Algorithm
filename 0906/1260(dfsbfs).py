'''
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

1000 1 1000
999 1000
'''


def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in G[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)


n, m, v = map(int, input().split())
G = [[0] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

dfs(v)