from collections import deque

n, m = map(int, input().split())
link = [[] for _ in range(n + 1)]
link_num = [0] * (n + 1)

for i in range(m):
    temp = list(map(int, input().split()))[1:]
    for j in range(1, len(temp)):
        link[temp[j - 1]].append(temp[j])
        link_num[temp[j]] += 1

q = deque()
for i in range(1, n + 1):
    if not link_num[i]:
        q.append(i)

result = []
while q:
    num = q.popleft()
    result.append(num)
    for i in link[num]:
        link_num[i] -= 1
        if not link_num[i]:
            q.append(i)

print(0 if len(result) != n else '\n'.join(map(str, result)))
