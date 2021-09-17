import sys

input = sys.stdin.readline

N = int(input())
max_num = 99999999
dp = [[[max_num] * 3 for _ in range(3)] for _ in range(N)]

mapp = []
for n in range(N):
    cost = list(map(int, input().split()))
    # 첫번째만 초기화
    if not n:
        for c in range(3):
            dp[n][c][c] = cost[c]
        continue

    for i in range(3):
        for j in range(3):
            min_dp = max_num
            for k in range(3):
                if k == i:  # 같은 색이면 제외
                    continue
                min_dp = min(dp[n - 1][k][j], min_dp)
            dp[n][i][j] = min_dp + cost[i]  # 이전의 최솟값 + 현재 색의 비용

result = max_num
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        result = min(result, dp[N - 1][i][j])
print(result)
