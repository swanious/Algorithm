from pprint import pprint

n, m = 12, 6

puyo = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

check_list = []
color_nums = 0
result = 0


def dfs(y, x):
    global color_nums, check_list
    color_nums += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or unlucky_visit[ny][nx]:
            continue

        if (ny, nx) in check_list:
            continue

        if puyo[ny][nx] == puyo[y][x]:
            check_list.append((ny, nx))
            dfs(ny, nx)


while True:
    unlucky_visit = [[False] * m for _ in range(n)]
    # 1. 돌다가 색을 만나면 dfs 돌기
    for i in range(n):
        for j in range(m):
            if puyo[i][j] == '.' or unlucky_visit[i][j]:
                continue
            else:
                check_list.append((i, j))
                dfs(i, j)
                # 1-1 dfs는 색의 개수가 4개 이상이면 visit 처리를 한다.
                if color_nums >= 4:
                    for y, x in check_list:
                        visit[y][x] = True
                        color_nums = 0
                        check_list = []
                else:
                    for y, x in check_list:
                        unlucky_visit[y][x] = True
                        color_nums = 0
                        check_list = []

    flag = False
    # 1-2 모든 dfs가 다 돌았을때, true인 곳을 .으로 변경한다.
    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                puyo[i][j] = '.'
                flag = True
                visit[i][j] = False

    # 종료) 1,2번를 반복하다가 visit에 더이상 true가 없으면 break를 한 후 result를 출력한다.
    if not flag:
        break

    result += 1

    # 2. 세로로 돌면서 색의 리스트를 받아놓은 후 한열씩 새로 그려준다.
    for i in range(m):
        temp = []
        for j in range(n):
            if puyo[j][i] != '.':
                temp.append(puyo[j][i])
        for j in range(n - 1, -1, -1):
            if temp:
                puyo[j][i] = temp.pop()
            else:
                puyo[j][i] = '.'

print(result)
