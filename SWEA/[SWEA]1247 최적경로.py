import sys

sys.stdin = open('input.txt')


def dfs(x, y, cnt):
    global minV

    if cnt > minV:
        return

    if 0 not in visited:
        cnt += abs(x - homeX) + abs(y - homeY)
        if minV > cnt:
            minV = cnt
        return

    for i in range(N):
        x1 = clients[i][0]
        y1 = clients[i][1]
        if not visited[i]:
            visited[i] = 1
            temp = abs(x - x1) + abs(y - y1)
            dfs(x1, y1, cnt + temp)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    tmp = list(map(int, input().split()))
    comX, comY, homeX, homeY = tmp[0], tmp[1], tmp[2], tmp[3]
    # 경로 만들기
    clients = []
    for i in range(2, N + 2):
        x = tmp[i * 2]
        y = tmp[i * 2 + 1]
        clients.append([x, y])

    visited = [0] * N  # 순열을 위한 visit 배열
    minV = 999999
    dfs(comX, comY, 0)
    print("#{} {}".format(tc, minV))