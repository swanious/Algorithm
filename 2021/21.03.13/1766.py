import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
link = [set() for _ in range(n + 1)]
link_num = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    link[a].add(b)
    link_num[b] += 1

q = []
for i in range(1, n + 1):
    if not link_num[i]:
        heapq.heappush(q, i)

while q:
    num = heapq.heappop(q)
    print(num, end=' ')
    for i in link[num]:
        link_num[i] -= 1
        if not link_num[i]:
            heapq.heappush(q, i)
