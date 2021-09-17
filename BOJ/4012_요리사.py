import sys

sys.stdin = open('sample_input.txt')


def calc(li):
    result = 0

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            result += arr[li[i]][li[j]] + arr[li[j]][li[i]]
    return result


def dfs(idx, k):
    global ans
    if idx == N // 2:
        A = []
        B = []
        for j in range(N):
            if visited[j]:
                A.append(j)
            else:
                B.append(j)
        recipe_A = calc(A)
        recipe_B = calc(B)

        if ans > abs(recipe_A - recipe_B):
            ans = abs(recipe_A - recipe_B)
        return

    for i in range(k, N):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, i + 1)
            visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    ans = 9999999

    dfs(0, 0)

    print("#{} {}".format(tc, ans))
