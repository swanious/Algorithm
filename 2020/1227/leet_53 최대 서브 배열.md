# leet_53 최대 서브 배열

- 합이 최대가 되는 서브 배열을 찾아 합을 반환

![image-20201228000824716](leet_53%20%EC%B5%9C%EB%8C%80%20%EC%84%9C%EB%B8%8C%20%EB%B0%B0%EC%97%B4.assets/image-20201228000824716.png)

- 과정

1. 누적합을 저장할 배열 생성

2. `배열의 현재 인덱스의 값(i)` + `누적합 배열의 이전 인덱스의 값(i - 1)`의 값을 sums 배열에 저장

   ​	2-1. 누적합 배열의 이전 인덱스의 값이 0보다 작으면 더해줄 필요가 없으므로 생략

3. max(sums) 반환

- 풀이 1

```python
class Solution(object):
    def maxSubArray(self, nums):
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)
        
```

- 풀이 2

```python
class Solution(object):
    def maxSubArray(self, nums):
        best_num = -sys.maxsize
        current_num = 0
        for num in nums:
            # 현재의 값 = max(배열의 값, 배열의 숫자 + 이전의 값)
            current_num = max(num, current_num + num)
            # 최적해 = max(지금까지의 최적해, 새로 구한 값)
            best_num = max(best_num, current_num)
            
        return best_num
```

