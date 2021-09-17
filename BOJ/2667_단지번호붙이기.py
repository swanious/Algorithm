'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

y, x = 0, 0
count = 1

def bfs(y, x):
    arr[y][x] = count
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if arr[ny][nx] == 1:
            arr[ny][nx] = count
            q.append((ny, nx))


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            y, x = i, j
            count += 1

            dy = [1, -1, 0, 0]
            dx = [0, 0, -1, 1]

            q = [(y, x)]

            while len(q) != 0:
                a = q.pop(0)
                bfs(a[0], a[1])

cnt = [0] * (count + 1)
cnt_num = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt[arr[i][j]] += 1
cnt.sort()

for i in cnt:
    if i != 0:
        cnt_num += 1
print(cnt_num)
for i in cnt:
    if i != 0:
        print(i)