### 문제

![image-20201231004532403](leet_238%20%EC%9E%90%EC%8B%A0%EC%9D%84%20%EC%A0%9C%EC%99%B8%ED%95%9C%20%EB%B0%B0%EC%97%B4%EC%9D%98%20%EA%B3%B1.assets/image-20201231004532403.png)

### 풀이

- 문제에서 보다시피 `나눗셈을 하지 않고 O(n)`으로 풀이를 해야한다. 즉, 미리 결과를 다 구해놓고, 자기 자신을 나누는 방식을 사용할 수 없다는 의미이다.
- 그럼, 자기 자신을 제외한 왼쪽 곱셈의 결과와 오른쪽 곱셈을 결과로 답을 구해야 한다.

```python
class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        result = []
        
        # 마지막을 제외한 왼쪽 곱셈의 결과 - [1, 1, 2, 6]
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]
        
        # 첫번째를 제외한 오른쪽 곱셈 결과 - [24, 12, 4, 1]
        # 둘을 곱하여 바로 답을 구한다. [1*24, 1*12, 2*4, 6*1]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= p
            p *= nums[i]
        
        return result
```

