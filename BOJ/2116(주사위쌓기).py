'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mapp = []
for i in range(n):
    new_li = []
    for j in range(6):
        if j == 0:
            new_li.append([arr[i][j], arr[i][5]])
        elif j == 1:
            new_li.append([arr[i][j], arr[i][3]])
        elif j == 2:
            new_li.append([arr[i][j], arr[i][4]])
        elif j == 3:
            new_li.append([arr[i][j], arr[i][1]])
        elif j == 4:
            new_li.append([arr[i][j], arr[i][2]])
        elif j == 5:
            new_li.append([arr[i][j], arr[i][0]])
    new_li.sort()
    mapp.append(new_li)

result = []
for i in range(6):
    num_sum = 0
    # 초기 밑면, 윗면 받아오기
    bottom = mapp[0][i][0]
    top = mapp[0][i][1]
    for j in range(n):  # 주사위 쌓기
        for k in range(6):
            if mapp[j][k][0] == bottom:
                top = mapp[j][k][1]
        if (bottom + top) == 11:
            num_sum += 4
        elif bottom == 6 or top == 6:
            num_sum += 5
        else:
            num_sum += 6
        bottom = top

    result.append(num_sum)

print(max(result))