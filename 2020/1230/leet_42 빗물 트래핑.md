문제 난이도가 너무 어려웠고 책 속의 코드를 봐도 이해하는데 오래걸렸다.

투 포인터를 하나씩 옮겨가면서 그려봤다..

![image-20201230155244143](leet_42%20%EB%B9%97%EB%AC%BC%20%ED%8A%B8%EB%9E%98%ED%95%91.assets/image-20201230155244143.png)

- 투 포인터

![image-20201230155901574](leet_42%20%EB%B9%97%EB%AC%BC%20%ED%8A%B8%EB%9E%98%ED%95%91.assets/image-20201230155901574.png)

즉, left와 right의 높이를 비교하면서 더 높은 곳을 향해 전진하면서 값을 구해나간다.

```python
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            # 빗물을 계산하기 위해 전 단계의 높이를 저장해둬야함
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # 더 높은 곳을 향해 투 포인터 이동
            if height[left] <= height[right]:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume
```

