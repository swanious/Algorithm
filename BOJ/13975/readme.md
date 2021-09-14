# 13975 파일 합치기
> [문제 링크](https://www.acmicpc.net/problem/13975)

## 설계
1. heapq 모듈을 사용해 pq생성
2. 크기가 작은 페이지 2개를 뽑아 더한 후 pq에 삽입
3. heap 길이가 1이 될때까지 2번 반복 및 minV에 저장
4. while문 종료되면 minV 출력

## 나의 코드
```python
from heapq import heapify, heappush, heappop
import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    costs = list(map(int, input().split()))
    heap = []

    for cost in costs:
        heap.append(cost)
    heapify(heap)
    
    minV = 0
    while len(heap) > 1:
        hap = heappop(heap) + heappop(heap)
        minV += hap
        heappush(heap, hap)

    print(minV)
```

## 후기
- 우선순위 큐를 만들면 쉽게 풀 수 있는 문제
- 불필요한 메모리 사용을 위해 항상 변수를 최소화하자