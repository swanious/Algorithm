# 주유소

![image-20201227024946051](leet_134.assets/image-20201227024946051.png)

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # 전체의 gas양보다 전체 cost양이 더 클 경우, 주유소를 돌 수 없으므로 return -1
        if sum(gas) < sum(cost):
            return -1
        
        # 출발지, 연료
        start, fuel = 0, 0
        for i in range(len(gas)):
            
            # 연료 + 채울 가스 보다 비용이 크면, 
            # 다음 주유소로 출발지 옮기기, 연료 초기화
            if fuel + gas[i] < cost[i]:
                start = i + 1 
                fuel = 0
                
            # 움직일 수 있으면, 연료 조정
            else:
                fuel += gas[i] - cost[i]
        return start
```

