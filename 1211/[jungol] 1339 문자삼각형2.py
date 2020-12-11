n, m = int(input()), 64
arr = [['' for _ in range(n)] for _ in range(n)]

# 제한 범위(1~100이하의 홀수)가 아니면, 에러
if n % 2 == 0 or n < 1 or n > 100:
    print("INPUT ERROR")

else:
    for i in range(n // 2, -1, -1):
        for j in range(i, (n // 2) * 2 - i + 1):
            if m >= 90:
                m = 64
            arr[j][i] = chr(m + 1)
            m += 1

    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                arr[i][j] = ' '
        print(*arr[i])
