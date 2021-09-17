T = int(input())
test = []
for i in range(T):
    test.append(int(input()))
n = max(test) + 1
dp = [[0] * 4 for _ in range(n + 1)]
dp[0] = [0, 0, 0, 0]
dp[1] = [1, 0, 0, 1]
dp[2] = [0, 1, 0, 1]
dp[3] = [1, 1, 1, 3]

for i in range(4, n):
    dp[i][0] = dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-2][0] + dp[i-2][2]
    dp[i][2] = dp[i-3][0] + dp[i-3][1]
    dp[i][3] = sum(dp[i][:3])

for i in test:
    print(dp[i][3])