import sys
sys.stdin = open('input.txt')

def getM(sy, sx):
    x = sx
    y = sy
    ex = 0
    while y < N and M[y][x] != 0: #y축(행의 변화)
        while x < N and M[y][x] != 0: # x축(열의 변화)
            M[y][x] = 0
            x += 1
        y+= 1
        ex = x - 1
        x = sx

    ey = y - 1
    size = (ey - sy + 1) * (ex - sx + 1)

    return size, ey-sy+1, ex-sx+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]


    lst = []
    for i in range(N):
        for j in range(N):
            if M[i][j] != 0:
                size, rc, cc = getM(i, j) # 스타트 지점
                lst.append((size, rc, cc))
    lst.sort()
    print(f'#{tc} {len(lst)}',end=' ')
    for i in range(len(lst)):
        print(lst[i][1], lst[i][2], end=' ')
    print()