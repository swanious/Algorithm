# 계단오르기

- 한번에 1, 2 계단을 오를 수 있다. 계단의 갯수 n이 주어질 때 계단을 오르는 경로의 수를 출력하라.
  - fibonacci 함수 => 메모이제이션을 활용하여 풀이

![image-20201228214850316](leet_70%20%EA%B3%84%EB%8B%A8%20%EC%98%A4%EB%A5%B4%EA%B8%B0.assets/image-20201228214850316.png)

```python
class Solution(object):
    dp = collections.defaultdict(int)

    def climbStairs(self, n):
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
```

