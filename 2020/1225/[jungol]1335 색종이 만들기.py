def div_conq(y, x, n):
    global b_cnt, w_cnt

    tmp = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if B[i][j]:
                tmp += 1

    if tmp == n ** 2:
        b_cnt += 1
    elif not tmp:
        w_cnt += 1
    else:
        # 분할정복
        div_conq(y, x, n // 2)  # y, x의 인덱스가 0~3일 때
        div_conq(y, x + n // 2, n // 2)  # y가 0~3, x가 4~7일 때
        div_conq(y + n // 2, x, n // 2)  # y가 4~7, x가 0~3일 때
        div_conq(y + n // 2, x + n // 2, n // 2)  # y가 4~7, x가 4~7일 때

    return


n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
b_cnt, w_cnt = 0, 0

div_conq(0, 0, n)
print(w_cnt)
print(b_cnt)