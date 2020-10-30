import sys;

sys.stdin = open('input.txt')


def maxProb(k, n, prob):
    global result
    if k == n:
        if prob > result:
            result = prob
            return

    if prob < result:
        return
    if prob == 0:
        return
    else:
        for i in range(n):
            if not visited[i] and arr[k][i]:
                visited[i] = True
                maxProb(k + 1, n, prob * arr[k][i] / 100)
                visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = 0
    maxProb(0, len(arr), 100)
    print('#{} {:.6f}'.format(tc, result))