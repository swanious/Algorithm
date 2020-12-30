### 문제

![image-20201231012308955](leet_121%20%EC%A3%BC%EC%8B%9D%EC%9D%84%20%EC%82%AC%EA%B3%A0%ED%8C%94%EA%B8%B0%20%EA%B0%80%EC%9E%A5%20%EC%A2%8B%EC%9D%80%20%EC%8B%9C%EC%A0%90.assets/image-20201231012308955.png)

### 풀이

- `무릎에서 사서 어깨에서 팔자`를 그대로 실천하면 된다. 우린 모든 값을 알고있으므로..

```python
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        minV = sys.maxsize
        
        for price in prices:
            minV = min(minV, price)
            profit = max(profit, price - minV)
        
        return profit
```

