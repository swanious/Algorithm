import sys
sys.stdin = open('sample_input.txt')


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(y, x):

    if arr[y][x] == 3:
        return 1
    # 처음 들어갔을때 1로 지우기
    arr[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if arr[ny][nx] == 1:
            continue
        # 첫 실수 : dfs(y, x)로 사용해서 처음의 좌표를 잃어버림..
        find = dfs(ny, nx)
        if find == 1:
            return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        s = input()
        new_li = []
        for j in range(N):
            new_li.append(int(s[j]))
        arr.append(new_li)


    y, x = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                y, x = i, j

    print("#{} {}".format(tc, dfs(y, x)))