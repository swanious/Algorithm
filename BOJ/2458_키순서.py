import sys

INF = sys.maxsize
n, m = map(int, input().split())
G = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1

# 경유지
for k in range(1, n+1):
    # 출발지
    for i in range(1, n+1):
        # 목적지
        for j in range(1, n+1):
            # 출발지 -> 경유지까지의 길이 있고,
            # 경유지 -> 목적지까지의 길이 있으면,
            if G[i][k] + G[k][j] == 2:
                G[i][j] = 1

# 경로가 있으면 +1
cnt = [0] * (n + 1)
for i in range(1, n+1):
    for j in range(1, n+1):
        if G[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1

print(cnt.count(n-1))