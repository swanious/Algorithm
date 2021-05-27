import pprint
'''
5 6
010101
010000
011101
100011
001011

8 8
11000111
01100000
00011001
11001000
10001001
10111100
01010000
00001011
'''

def dfs(y, x):
    # 맨 처음에는 이놈이 맨 끝값이면(전기가 흐르면) return 1
    if y == iny-1:
        return 1
    # 처음 시작하면 밟은 땅을 1로 (돌아오지 않기 위해서)
    li[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny <0 or nx >= inx or ny >= iny:
            continue

        if li[ny][nx] == 1:
            continue

        find = dfs(ny, nx)
        # 내가 원하는 목적지에 도달했을 때, return 1
        if find == 1:
            return 1

    # 만약에 찾지 못했으면, 밟은 땅들을 0으로 초기화시켜주고 돌아감
    li[y][x] = 0
    return 0

iny, inx = map(int,input().split())
li = []
for i in range(iny):
    s = input()
    newli = []
    for j in range(inx):
        newli.append(int(s[j]))
    li.append(newli)

isfind = 0
for i in range(inx):
    isfind = dfs(0, i)
    if(isfind == 1):
        break
if isfind == 1: print("YES")
else: print("NO")