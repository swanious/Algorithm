from collections import deque

q = deque()
n, m = map(int, input().split())
visited = [False] * 100001
save = 0
temp = 0
q.append([n, 0])

while q:
    v = q.popleft()
    if v[0] == m:
        save = v[1]
        break

    for i in range(3):
        if i == 0:
            temp = v[0] * 2
            if 0 <= temp <= 100000 and not visited[temp]:
                visited[temp] = True
                q.appendleft([temp, v[1]])
                continue
        elif i == 1:
            temp = v[0] + 1
        elif i == 2:
            temp = v[0] - 1
        if temp < 0 or temp > 100000:
            continue
        if visited[temp]:
            continue
        visited[temp] = True
        q.append([temp, v[1] + 1])
print(save)