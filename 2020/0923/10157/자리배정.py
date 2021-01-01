'''
7 6
11
'''
h, w = map(int, input().split())
stand = int(input())
arr = [[0] * w for _ in range(h)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

ny, nx, y, x = 0, 0, 0, 0
idx = 0
num = 1
result = []

for _ in range(h * w):
    y, x = ny, nx
    if num == stand:
        result.append(y + 1)
        result.append(x + 1)
        break

    arr[y][x] = num

    # 첫 방향 설정
    ny = y + dy[idx]
    nx = x + dx[idx]

    # 방향 전환
    if ny < 0 or ny >= h or nx < 0 or nx >= w or arr[ny][nx] != 0:
        idx = (idx + 1) % 4
        ny = y + dy[idx]
        nx = x + dx[idx]
    num += 1

if stand > (h * w):
    print(0)
else:
    print(*result)
