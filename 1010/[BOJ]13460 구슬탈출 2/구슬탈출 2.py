'''
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########
'''

from collections import deque

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

red = []
blue = []
ball_map = tuple()
cnt = -1

visit = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            arr[i][j] = 2

        elif arr[i][j] == 'O':
            arr[i][j] = 1

        elif arr[i][j] == '.':
            arr[i][j] = 0

        elif arr[i][j] == 'R':
            arr[i][j] = 0
            red.append(i)
            red.append(j)

        elif arr[i][j] == 'B':
            arr[i][j] = 0
            blue.append(i)
            blue.append(j)

# 4방향 설정
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


# bfs 함수
def bfs(rry, rrx, bby, bbx, count):
    global cnt, q
    count += 1

    # 제약1. count가 10이하인 경우만 돌아야함
    if count > 10:
        cnt = -1
        q = []
        return

    for i in range(4):
        ry = rry
        rx = rrx
        by = bby
        bx = bbx

        ry, rx = straight(ry, rx, by, bx, i)
        by, bx = straight(by, bx, ry, rx, i)
        ry, rx = straight(ry, rx, by, bx, i)

        # 제약2. blue가 홀에 들어가면 안됨
        if arr[by][bx] == 1:
            cnt = -1
            continue

        # 결과. 빨간공이 들어가면 cnt를 반환하고, 더이상 q를 볼필요 없으므로 q를 비워주고 return
        elif arr[ry][rx] == 1:
            cnt = count
            q = []
            return

        if visit[ry][rx][by][bx] == True:
            continue
        visit[ry][rx][by][bx] = True
        q.append((ry, rx, by, bx, count))


def straight(moveY, moveX, stopY, stopX, dir):
    # 현재 위치를 저장해줌 - 제약 사항을 판단하기 위해
    y, x = moveY, moveX
    ny = y + dy[dir]
    nx = x + dx[dir]
    while True:
        # 벽과 만났을 때
        if arr[ny][nx] == 2:
            break

        # 공과 공이 만났을 때
        elif ny == stopY and nx == stopX:
            if arr[ny][nx] == 1:
                y = ny
                x = nx
                break
            break

        # 홀인원 - 자기 위치가 홀이면, break 후 bfs함수로 리턴해준다.
        elif arr[y][x] == 1:
            break

        y = ny
        x = nx
        ny = y + dy[dir]
        nx = x + dx[dir]
    return y, x


ball_map = (red[0], red[1], blue[0], blue[1], 0)
# 큐 받아주기
q = deque()
visit[red[0]][red[1]][blue[0]][blue[1]] = True
q.append(ball_map)


# 뽑아주기
def split_str(a, b, c, d, e):
    q.append((a, b, c, d, e))


split_str(*q[0])

while len(q) != 0:
    bfs(*q.popleft())

print(cnt)