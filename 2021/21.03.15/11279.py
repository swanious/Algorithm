import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    m = int(input())
    if not m: # 값이 0이면
        if not len(q):
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -m)

