import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    k = 0
    result = 0

    for i in range(n):
        for j in range(mid-k, mid+k+1):
            result += arr[i][j]
        if i < mid:
            k += 1
        else:
            k -= 1
    print("#{} {}".format(tc, result))
