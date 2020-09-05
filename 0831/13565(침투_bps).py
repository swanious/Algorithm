dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(new_li):
    global check
    y, x = new_li[0], new_li[1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= iny or nx < 0 or nx >= inx:
            continue
        if li[ny][nx] == 1:
            continue
        if ny == iny - 1:
            check = True
        li[ny][nx] = 1
        result.append([ny, nx])

iny, inx = map(int, input().split())
li = []
check = False
# 데이터 받기
for i in range(iny):
    s = input()
    newli = []
    for j in range(inx):
        newli.append(int(s[j]))
    li.append(newli)

result = []
for i in range(inx):
    result.append([0, i])
    # 초기 점 (다시 돌아오면 안되니까 1로 만들어주기)
    li[0][i] = 1
    while len(result) != 0:
        new_li = result[0]
        result = result[1:]
        bfs(new_li)

if check == True:
    print("YES")
else:
    print("NO")