'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

sum_mapp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        left = 0
        up = 0
        left_up = 0
        if i - 1 >= 0:  # 맨 위가 아니면(인덱스 오류 방지)
            up = sum_mapp[i - 1][j]
        if j - 1 >= 0:  # 맨 왼쪽이 아니면(인덱스 오류 방지)
            left = sum_mapp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:  # 맨 위, 왼쪽 끝이 아니면(인덱스 오류 방지)
            left_up = sum_mapp[i - 1][j - 1]
        sum_mapp[i][j] = mapp[i][j] + left + up - left_up

result = 0
for i in range(m):
    sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
    if not sy and not sx:
        result = sum_mapp[ey][ex]
    elif not sy and sx:
        result = sum_mapp[ey][ex] - sum_mapp[ey][sx - 1]
    elif not sx and sy:
        result = sum_mapp[ey][ex] - sum_mapp[sy - 1][ex]
    else:
        result = sum_mapp[ey][ex] - sum_mapp[ey][sx - 1] - sum_mapp[sy - 1][ex] + sum_mapp[sy - 1][sx - 1]
    print(result)
