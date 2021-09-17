import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    min_arr, max_arr = [], []
    visit = [False] * n
    for i in range(n):
        operand, num = input().split()
        num = int(num)
        # 삽입
        if operand == 'I':
            heapq.heappush(min_arr, (num, i))
            heapq.heappush(max_arr, (-num, i))

        # 최댓값 삭제
        elif num == 1:
            if not len(max_arr):
                continue
            else:
                _, idx = heapq.heappop(max_arr)
                visit[idx] = True

        # 최솟값 삭제
        else:
            if not len(min_arr):
                continue
            else:
                _, idx = heapq.heappop(min_arr)
                visit[idx] = True

        # max_arr, min_arr의 visit가 True이면 삭제
        while max_arr:
            num, idx = heapq.heappop(max_arr)
            if not visit[idx]:
                heapq.heappush(max_arr, (num, idx))
                break
        while min_arr:
            num, idx = heapq.heappop(min_arr)
            if not visit[idx]:
                heapq.heappush(min_arr, (num, idx))
                break

    if not len(max_arr):
        print('EMPTY')
    else:
        print(-heapq.heappop(max_arr)[0], heapq.heappop(min_arr)[0])