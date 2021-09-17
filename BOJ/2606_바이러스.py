'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''


def dfs(v):
    visit[v] = 1
    for w in G[v]:
        if not visit[w]:
            visit[w] = 1
            dfs(w)


n = int(input())
m = int(input())
G = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dfs(1)

print(visit.count(1) - 1)
