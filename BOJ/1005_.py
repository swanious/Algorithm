from collections import deque

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    link = [set() for _ in range(n + 1)]
    rev_link = [set() for _ in range(n + 1)]
    degree = [0] * (n + 1)
    result = [0] * (n + 1)
    for i in range(k):
        start, end = map(int, input().split())
        link[start].add(end)
        rev_link[end].add(start)
        degree[end] += 1

    obj = int(input())

    degree[0] = -1
    q = deque()
    for i, value in enumerate(degree):
        if not value:
            q.append(i)

    while q:
        point = q.popleft()
        max_num = 0
        for i in rev_link[point]:
            max_num = max(max_num, result[i])
        result[point] = max_num + time[point]
        if point == obj:
            break
        for i in link[point]:
            degree[i] -= 1
            if not degree[i]:
                q.append(i)

    print(result[obj])