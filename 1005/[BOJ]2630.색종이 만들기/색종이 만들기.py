'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''

import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

blue_cnt = 0
white_cnt = 0

def cut(n, y, x):
    global blue_cnt, white_cnt
    count = 0
    # 1. count로 2중 for문 돌면서, 0, n**2 인지 확인
    for i in range(y, n + y):
        for j in range(x, n + x):
            count += arr[i][j]

    # 2. count 값이 0이면 white 증가
    if count == 0:
        white_cnt += 1
        return

    # 3. count 값이 1이면 blue 증가
    elif count == n ** 2:
        blue_cnt += 1
        return

    # 4. 그 외의 count 값이면 4부분으로 잘라서 재귀함수 호출
    else:
        cut(n // 2, y, x)
        cut(n // 2, y + n // 2, x)
        cut(n // 2, y, x + n // 2)
        cut(n // 2, y + n // 2, x + n // 2)

cut(n, 0, 0)
print(white_cnt)
print(blue_cnt)