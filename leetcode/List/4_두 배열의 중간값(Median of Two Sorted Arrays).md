### 문제

> Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.
>
> The overall run time complexity should be `O(log (m+n))`.
>
> **두 배열을 합쳐서 중간값을 찾아라.**

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

### 풀이

- 두 배열을 더해서 파이썬의 `sorted`함수를 사용하여 합친 후,

- 짝/ 홀일 때를 나눠서 구해줬다.

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sortedArray = sorted(nums1 + nums2)
        length = len(sortedArray)
        res = 0
        # 짝수
        if length % 2 == 0:
            res = (sortedArray[(length//2) - 1] + sortedArray[length//2]) / 2
        # 홀수
        else:
            res = sortedArray[length//2]
        return res
```