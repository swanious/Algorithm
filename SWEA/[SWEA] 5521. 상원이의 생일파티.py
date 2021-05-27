'''
2
6 5
2 3
3 4
4 5
5 6
2 5
6 5
1 2
1 3
3 4
2 3
4 5
'''

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    cnt = 0
    q = deque()
    q.append((1, 0))  # 상원이(1), 거리 저장
    visited[1] = True
    while q:
        v = q.popleft()
        if v[1] == 2:  # 상원이와 떨어진 거리가 2라면 break
            break
        for w in G[v[0]]:
            if not visited[w]:
                cnt += 1
                visited[w] = True
                q.append((w, v[1] + 1))

    print("#{} {}".format(tc, cnt))
