from collections import deque

n, m = map(int, input().split())
link = {}
for _ in range(m):
    st, ed = input().split()
    link[st] = link.get(st, set())
    link[st].add(ed)

Q = int(input())
for query in range(Q):
    a, b = input().split()
    q = deque()
    q.append(a)
    signal = False
    while q:
        name = q.popleft()
        if not link.get(name, 0):
            continue
        for i in link[name]:
            q.append(i)
            if i == b:
                print(a, end=' ')
                signal = True
            if signal:
                break
        if signal:
            break
    if signal:
        continue

    q = deque()
    q.append(b)
    signal = False
    while q:
        name = q.popleft()
        if not link.get(name, 0):
            continue
        for i in link[name]:
            q.append(i)
            if i == a:
                print(b, end=' ')
                signal = True
            if signal:
                break
        if signal:
            break
    if signal:
        continue

    print('gg', end=' ')
