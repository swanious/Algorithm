n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

# 앞에 애들은 이미 졸라 잘 구해줌
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] = dp[i] % 10007

print(dp[n])