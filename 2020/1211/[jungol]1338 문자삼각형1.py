n, m = int(input()), 64
arr = [['' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n - i - 1):
        arr[i][j] = ' '

    k = n-1
    for j in range(i, k):
        arr[j][k] = chr(m+1)
        m += 1
        k -= 1

for i in range(n):
    print(*arr[i])
print(arr)