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
