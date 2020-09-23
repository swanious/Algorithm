import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    # 최종 합
    result = []

    # 가로 합
    garo_total = []
    for i in range(100):
        garo = 0
        for j in range(100):
            garo += arr[i][j]
        garo_total.append(garo)
    result.append(max(garo_total))

    # 세로 합
    sero_total = []
    for i in range(100):
        sero = 0
        for j in range(100):
            sero += arr[j][i]
        sero_total.append(sero)
    result.append(max(sero_total))

    # 대각 합
    i, j, dae1, dae2 = 0, 0, 0, 0
    while i < 100:
        dae1 += arr[i][i]
        i += 1
    while i < 100 and j < 100:
        dae2 += arr[i][100-j-1]
        i += 1
        j += 1

    result.append(dae1)
    result.append(dae2)

    print("#{} {}".format(tc, max(result)))