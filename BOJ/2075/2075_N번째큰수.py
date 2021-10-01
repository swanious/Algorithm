import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
cnt = 0
for _ in range(N):
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
print(heap[0])