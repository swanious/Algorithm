import sys
import heapq

input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    m = int(input())
    if not m:
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, m)