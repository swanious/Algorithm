'''
5 5
1 1 1
1 1 2
1 2 2
1 2 3
3 1
'''
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
train = [0] * n
cnt = 0
for i in range(m):
    order = list(map(int, sys.stdin.readline().rstrip().split()))
    order[1] = order[1] - 1
    if order[0] == 1:
        order[2] = 20 - order[2]
        if (train[order[1]] & (1 << order[2])) == 0:
            train[order[1]] += (1 << order[2])
    elif order[0] == 2:
        order[2] = 20 - order[2]
        if (train[order[1]] & (1 << order[2])) > 0:
            train[order[1]] -= (1 << order[2])
    elif order[0] == 3:
        train[order[1]] = train[order[1]] >> 1

    elif order[0] == 4:
        if (train[order[1]] & (1 << 19)) > 0:
            train[order[1]] -= (1 << 19)
        train[order[1]] = train[order[1]] << 1

cnt = len(set(train))
print(cnt)
