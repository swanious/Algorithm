import sys

input = sys.stdin.readline

n, h, d = map(int, input().split()) # 배열크기, 체력, 우산내구도
mapp = [input() for _ in range(n)]

result = sys.maxsize
sy, sx = 0, 0
ey, ex = 0, 0
u_list = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 'S':
            sy, sx = i, j
        elif mapp[i][j] == 'E':
            ey, ex = i, j
        elif mapp[i][j] == 'U':
            u_list.append((i, j))

visit = [False] * len(u_list)

def get_distance(ey, ex, y, x):
    return abs(ey - y) + abs(ex - x)

def dfs(y, x, life, shield, count):
    global result

    if get_distance(ey, ex, y, x) <= life + shield:
        result = min(result, count + get_distance(ey, ex, y, x))
        return 

    for i in range(len(u_list)):
        uy, ux = u_list[i]
        dis = get_distance(uy, ux, y, x)
        if life + shield <= dis - 1 or visit[i]:
            continue
        
        if shield < dis:
            visit[i] = True
            dfs(uy, ux, life - (dis - shield), d, count + dis)
            visit[i] = False

        else:
            visit[i] = True
            dfs(uy, ux, life, d, count + dis)
            visit[i] = False

dfs(sy, sx, h, 0, 0)
print(-1 if result == sys.maxsize else result)