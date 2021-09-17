# 입력
n, m, y, x, k = map(int, input().split())
mapp = [[0] * m for _ in range(n)]
dice = [[0] * 3 for _ in range(4)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        mapp[i][j] = temp[j]

# 맨 밑 숫자 초기화
dice[3][1] = mapp[y][x]
order = list(map(int, input().split()))

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]


def change_dice(d):
    global dice

    if d == 1:
        dice[1][2], dice[3][1], dice[1][1], dice[1][0] = dice[3][1], dice[1][0], dice[1][2], dice[1][1]
    elif d == 2:
        dice[1][2], dice[3][1], dice[1][1], dice[1][0] = dice[1][1], dice[1][2], dice[1][0], dice[3][1]
    elif d == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    else:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]


for i in order:
    ny = y + dy[i]
    nx = x + dx[i]

    # 벽 체크
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue

    y, x = ny, nx
    if not mapp[y][x]:
        change_dice(i)
        mapp[y][x] = dice[3][1]

    else:
        change_dice(i)
        dice[3][1] = mapp[y][x]
        mapp[ny][nx] = 0
    print(dice[1][1])
