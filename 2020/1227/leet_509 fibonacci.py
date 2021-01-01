from collections import defaultdict


# 기본 풀이 - 1048 ms
class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


# 메모이제이션(하향식, 재귀) - 12 ms
class Solution(object):
    dp = defaultdict(int)

    def fib(self, n):
        # memoization
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# 타뷸레이션(상향식, 반복문) - 20 ms
class Solution(object):
    dp = defaultdict(int)

    def fib(self, n):
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]

# 두 변수만을 이용 - 12 ms
class Solution(object):
    def fib(self, n):
        x, y = 0, 1
        for i in range(0, n):
            x, y = x, x + y
        return x