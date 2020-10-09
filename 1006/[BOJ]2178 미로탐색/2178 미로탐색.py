'''
4 6
101111
101010
101011
111011
'''

# 입력
n, m = map(int, input().split())
arr = []
for i in range(n):
    s = input()
    s_list = []
    for j in s:
        s_list.append(int(j))
    arr.append(s_list)

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

q = [(0, 0)]

def bfs(y, x):
    # 4 방향서치 후 1을 찾으면,
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > ny or ny >= n or 0 > nx or nx >= m:
            continue
        # 방향을 전환한다.
        if arr[ny][nx] == 1:
            arr[ny][nx] = arr[y][x] + 1
            q.append((ny, nx))
while len(q) != 0:
    a = q.pop(0)
    bfs(a[0], a[1])

print(arr[n-1][m-1])