import sys
from collections import deque

n = int(sys.stdin.readline().strip())

# 첫 시도는 list.pop(0) 형식으로 list를 통한 풀이를 사용했다.
# 그 결과 시간초과..
# 그보다 훨씬 빠른 deque()의 존재를 알고, 바로 사용해봤다.
deq = deque()
for i in range(1, n+1):
    deq.append(i)


while len(deq) != 1:
    deq.popleft()
    a = deq.popleft()
    deq.append(a)

print(*deq)