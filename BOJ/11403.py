from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

G = {}
for i in range(n):
    G[i] = []
    for j in range(n):
        if arr[i][j] == 1:
            G[i].append(j)

q = deque()
for i in range(len(G)):
    q.append(i)
    visit = [0] * len(G)
    while q:
        start = q.popleft()
        for w in G[start]:
            if visit[w] == 0:
                visit[w] = 1
                arr[i][w] = 1 #
                q.append(w)
for i in range(len(arr)):
    print(*arr[i])

'''
3
0 1 0
0 0 1
1 0 0
'''