import sys

sys.stdin = open('input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    mapp = [list(input()) for _ in range(H)]
    N = int(input())
    commands = list(input())

    y, x, di = 0, 0, 0

    # 전차의 위치 및 방향
    for i in range(H):
        for j in range(W):
            if mapp[i][j] == '^':
                y, x, di = i, j, 0
            elif mapp[i][j] == 'v':
                y, x, di = i, j, 1
            elif mapp[i][j] == '<':
                y, x, di = i, j, 2
            elif mapp[i][j] == '>':
                y, x, di = i, j, 3

    for command in commands:
        if command == 'S':
            ny = y + dy[di]
            nx = x + dx[di]
            while True:
                if 0 <= ny < H and 0 <= nx < W:
                    if mapp[ny][nx] == '.' or mapp[ny][nx] =='-':
                        ny = ny + dy[di]
                        nx = nx + dx[di]
                    elif mapp[ny][nx] == '#':
                        break
                    elif mapp[ny][nx] == '*':
                        mapp[ny][nx] = '.'
                        break
                else:
                    break

        # 상, 하, 좌, 우 움직임
        elif command == 'U':
            di = 0
            if 0 <= (y - 1) < H and mapp[y - 1][x] == '.':
                mapp[y][x] = '.'
                y = y - 1
                mapp[y][x] = '^'
            else:
                mapp[y][x] = '^'
        elif command == 'D':
            di = 1
            if 0 <= (y + 1) < H and mapp[y + 1][x] == '.':
                mapp[y][x] = '.'
                y = y + 1
                mapp[y][x] = 'v'
            else:
                mapp[y][x] = 'v'
        elif command == 'L':
            di = 2
            if 0 <= (x - 1) < W and mapp[y][x - 1] == '.':
                mapp[y][x] = '.'
                x = x - 1
                mapp[y][x] = '<'
            else:
                mapp[y][x] = '<'
        elif command == 'R':
            di = 3
            if 0 <= (x + 1) < W and mapp[y][x + 1] == '.':
                mapp[y][x] = '.'
                x = x + 1
                mapp[y][x] = '>'
            else:
                mapp[y][x] = '>'

    print('#{}'.format(tc), end=' ')
    for i in range(H):
        print("".join(mapp[i]))