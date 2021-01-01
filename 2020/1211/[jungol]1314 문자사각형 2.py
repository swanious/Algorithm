n, m = int(input()), 64
arr = [['' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if m >= 90:
            m = 64

        # 행, 열 전환
        # 홀수 열,
        if i % 2:
            arr[n-j-1][i] = chr(m + 1)
            m += 1
        # 짝수 열,
        else:
            arr[j][i] = chr(m + 1)
            m += 1

for i in range(n):
    print(*arr[i])