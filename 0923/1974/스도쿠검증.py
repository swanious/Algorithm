import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    count = 0

    # 3 X 3 정사각형
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count_list = [0] * 10
            for y in range(3):
                for x in range(3):
                    count_list[arr[y][x]] += 1
            if count_list.count(0) != 1:
                count += 1

    # 1 X 9 직사각형
    for i in range(9):
        count_list = [0] * 10
        for j in range(9):
            count_list[arr[i][j]] += 1
        if count_list.count(0) != 1:
            count += 1


    # 9 X 1 직사각형
    for i in range(9):
        count_list = [0] * 10
        for j in range(9):
            count_list[arr[j][i]] += 1
        if count_list.count(0) != 1:
            count += 1

    if count >= 1:
        print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, 1))