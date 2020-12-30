### 투 포인터로 문제해결

- 문제
  - 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력

![image-20201231002951146](leet_15%203Sum.assets/image-20201231002951146.png)

```python
def threeSum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복 값 미리 제거
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격 좁혀가며 합 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
				
                # 합이 0인 경우, 동일한 값은 볼 필요없으므로 skip
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result
nums = [-1,0,1,2,-1,-4]
ans = []
ans = threeSum(nums)
print(ans)
```

