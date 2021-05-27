n, m = map(int, input().split())
arr = []
visit = [False] * (n + 1)


def dfs(v):
    global visit
    
    if len(arr) == m:
        print(*arr)
        return

    else:
        for i in range(1, n + 1):
            if not visit[i]:
                visit[i] = True
                arr.append(i)
                dfs(i + 1)
                arr.pop()
                visit[i] = False


dfs(1)
