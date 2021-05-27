'''
3
3
111
4
1101
5
11111
'''
T = int(input())
for tc in range(T):
    input()
    M = list(map(int, list(input())))
    dp = [0] * len(M)
    dp[0] = 1
    for i in range(1, len(M)):
        if M[i] == 1:
            dp[i] = dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
        else:
            dp[i] = 0

    print(dp[len(M) - 1])
