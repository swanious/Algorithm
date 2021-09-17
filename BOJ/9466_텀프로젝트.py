def dfs(num):
    stack = []
    stack.append(num)
    while stack:
        v = stack[-1]
        if v in cycle_dict:
            for j in range(cycle_dict[v]):
                visit[stack[j]] = 2
            for j in range(cycle_dict[v], len(stack)):
                visit[stack[j]] = 1
            return
        if visit[find_team[v]] != 0:
            for s in stack:
                visit[s] = 2
            return
        cycle_dict[v] = len(stack)
        stack.append(find_team[v])


for _ in range(int(input())):
    n = int(input())
    find_team = [0] * (n + 1)
    visit = [0] * (n + 1)
    temp = list(map(int, input().split()))
    for i in range(1, n + 1):
        find_team[i] = temp[i - 1]

    for i in range(1, n + 1):
        if visit[i] == 1 or visit[i] == 2:
            continue
        cycle_dict = dict()
        temp = i
        dfs(i)
    print(visit.count(2))
