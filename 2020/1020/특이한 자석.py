import sys
from collections import deque

sys.stdin = open('sample_input.txt')


def rotate(n, d):
    if d == 1:
        s = magmap[n][-1]
        e = magmap[n][:-1]
        magmap[n] = [s] + e
    else:
        s = magmap[n][0]
        e = magmap[n][1::]
        magmap[n] = e + [s]


T = int(input())
for t in range(1, T + 1):

    k = int(input())
    magmap = [list(map(int, input().split())) for _ in range(4)]

    # 명령어 만큼 회전
    for i in range(k):
        no, di = map(int, input().split())
        no -= 1
        direction = [0] * 4  # 돌 수 있는지 여부
        direction[no] = di
        # 칼날의 오른 쪽 것들이 회전 가능한지 확인하고 rotate
        for j in range(no + 1, 4):
            if magmap[j - 1][2] != magmap[j][6]:
                direction[j] = -direction[j - 1]
            else:
                break

        # 칼날의 왼쪽 것들이 회전 가능한지 확인하고 rotate
        for j in range(no - 1, -1, -1):
            if magmap[j + 1][6] != magmap[j][2]:
                direction[j] = -direction[j + 1]
            else:
                break

        for j in range(4):
            if direction[j] == 1:
                rotate(j, direction[j])
            elif direction[j] == -1:
                rotate(j, direction[j])

    # 결과 값
    result = [1, 2, 4, 8]
    for i in range(4):
        result[i] *= magmap[i][0]
    print('#{} {}'.format(t, sum(result)))
