import sys;

sys.stdin = open('input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, skill, count):
    global max_length

    max_length = max(max_length, count)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            # 다음이 나보다 작은 경우
            if mapp[ny][nx] < mapp[y][x]:
                visited[ny][nx] = True
                dfs(ny, nx, skill, count + 1)
                visited[ny][nx] = False
                
            # 공사를 하면 현재 위치의 높이보다 작아지는 경우
            elif mapp[ny][nx] - skill < mapp[y][x]:
                visited[ny][nx] = True
                tmp = mapp[ny][nx]
                mapp[ny][nx] = mapp[y][x] - 1
                dfs(ny, nx, 0, count + 1)
                mapp[ny][nx] = tmp
                visited[ny][nx] = False


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(n)]
    
    # 제일 높은 높이 구하기
    maxV = 0
    for i in range(n):
        maxV = max(maxV, max(mapp[i]))
    
    # dfs 돌리기
    max_length = 0
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == maxV:
                visited = [[False] * n for _ in range(n)]
                visited[i][j] = True
                dfs(i, j, k, 1)
    print('#{} {}'.format(tc, max_length))