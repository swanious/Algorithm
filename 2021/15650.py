n, m = map(int, input().split())
arr = []
visit = [False] * (n + 1)


def dfs(v):
    global visit

    if len(arr) == m:
        print(*arr)
        return

    else:
        # 15649번과 다른 점은 1부터 돌지말고 v부터 도는 것 !
        for i in range(v, n + 1):
            if not visit[i]:
                visit[i] = True
                arr.append(i)
                dfs(i + 1)
                arr.pop()
                visit[i] = False



dfs(1)
