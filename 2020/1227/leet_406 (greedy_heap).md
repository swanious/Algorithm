# leet_406 키에 따른 대기열 재구성

- 우선순위큐를 통해 푼다.
- 파이썬의 heap은 항상 최소힙이므로, 역수를 넣어준 후, 꺼낼 때 다시 역수로 넣어줘서 뽑아낸다.(최대힙으로 변환)

```python
class Solution(object):
    def reconstructQueue(self, people):

        heap = []
        # 키(person[0])의 역수를 집어넣어줌
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            # person[1] : 앞에 자신의 키 이상인 사람의 수
            # 즉, person[1]을 인덱스로 활용하여 insert를 통해 구현하면 쉽게 풀이가 가능
            result.insert(person[1], (-person[0], person[1]))
        return result
```

