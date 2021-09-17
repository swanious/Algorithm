'''
3 3
1 2 1
2 3 2
1 3 3
'''


def prim():
    D = [inf] * (v + 1)
    u = [0]
    D[0] = 0
    for i in range(v + 1):
        D[i] = adj[0][i]

    while len(u) <= v:
        minV = inf
        min_idx = -1
        for i in range(v + 1):
            if i in u:
                continue
            if minV > D[i]:
                minV = D[i]
                min_idx = i

        u.append(min_idx)

        for i in range(v+1):
            if i in u:
                continue
            if D[i] > adj[min_idx][i]:
                D[i] = adj[min_idx][i]


inf = 2147483647
v, e = map(int, input().split())
adj = [[inf] * (v + 1) for _ in range(v + 1)]

for i in range(e):
    a, b, w = map(int, input().split())
    adj[a][b] = w
    adj[b][a] = w

prim()