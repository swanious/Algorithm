'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
'''
from collections import deque


def bfs(v):
    q.append((v, 0))
    visited = [False] * (n + 1)
    visited[v] = True
    level = 999
    while q:
        v, level = q.popleft()
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                q.append((w, level+1))
    return level

n = int(input())

q = deque()
# 인접 리스트
G = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    G[a].append(b)
    G[b].append(a)

# 결과값 찾기
result_score = 999
result = []
for i in range(1, n + 1):
    score = bfs(i)
    print(score)
    if score < result_score:
        if result:
            result = []
        result.append(i)
        result_score = score
    elif score == result_score:
        result.append(i)
print(result_score, len(result))
for i in result:
    print(i, end=' ')
