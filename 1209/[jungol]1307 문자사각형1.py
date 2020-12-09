n = int(input())
arr = [[0] * n for _ in range(n)]
alpha = 64
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        arr[j][i] = chr(alpha + 1)
        alpha += 1
        if alpha == 90:
            alpha = 64

for i in range(n):
    print(*arr[i])

'''
출력 예
P L H D
O K G C
N J F B
M I E A
'''