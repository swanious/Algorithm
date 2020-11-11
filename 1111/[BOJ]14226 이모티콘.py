from collections import deque

n = int(input())

q = deque([(1, 0)])

visited = dict()
visited[(1, 0)] = 0
while q:
    v, c = q.popleft()
    if v == n:
        print(visited[(v, c)])
        break
    if (v, v) not in visited and 1 <= v < 2001:
        visited[(v, v)] = visited[(v, c)] + 1
        q.append((v, v))
    if (v - 1, c) not in visited and 1 <= v-1 < 2001 and 1 <= c < 2001:
        visited[(v - 1, c)] = visited[(v, c)] + 1
        q.append((v - 1, c))
    if (v + c, c) not in visited and 1 <= v+c < 2001 and 1 <= c < 2001:
        visited[(v + c, c)] = visited[(v, c)] + 1
        q.append((v + c, c))
