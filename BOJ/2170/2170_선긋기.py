import sys

input = sys.stdin.readline
lines = []

for i in range(int(input())):
    lines.append(list(map(int, input().split())))

lines.sort(key = lambda x: x[0])

check = False
start, end = 0, 0
ans = 0

for line in lines:
    if not check:
        start = line[0]
        end = line[1]
        check = True
        continue

    if line[0] <= end:
        end = max(end, line[1])

    else:
        ans += end - start
        start = line[0]
        end = line[1]
        
ans += end - start
print(ans)