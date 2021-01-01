def dfs(idx):
    for i in range(1, (idx // 2) + 1):
        if ans[-i:] == ans[-2*i:-i]: return -1
    if idx == n:
        for i in range(n):
            print(ans[i], end='')
        return 0

    for i in range(1, 4):
        ans.append(i)
        if dfs(idx + 1) == 0:
            return 0
        ans.pop()


n = int(input())
ans = []
dfs(0)
