## 문제

> 347. Top K Frequent Elements
>
> 빈도수가 k이상인 숫자를 배열에 담아 출력

Given a non-empty array of integers, return the ***k\*** most frequent elements.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Note:**

- You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
- Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.
- It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
- You can return the answer in any order.



## 풀이

1. heapq
   - heapq를 이용하여 최대힙을 구현
   - 최대힙의 요소를 k만큼 돌면서 key를 pop한다.

```python
class Solution(object):
    def topKFrequent(self, nums, k):

        count_heap = []
        count = collections.Counter(nums)
        
        for c in count:
            # heap은 키 순서대로 정렬되므로, 키/값을 바꿔서 힙에 추가(key:c, value:count[k])
            # heapq는 기본적으로 최소힙이므로, -를 통해 최대힙으로 변환
            heapq.heappush(count_heap, (-count[c], c))
            
        result = list()
        for _ in range(k):
            result.append(heapq.heappop(count_heap)[1])
        return result
```

2. python다운 풀이
   - collections.Counter()에 most_common()이라는 유용한 함수를 사용

```python
def topKFrequency(self, nums, k):
    # zip으로 key값을 모두 뽑아내서 출력
    return list(*zip(collections.Counter(nums).most_common(k)))[0]
```

