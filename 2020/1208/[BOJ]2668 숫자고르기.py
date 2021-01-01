n = int(input())
mapp = [0]
result = [False] * (n + 1)
visit_set = set()

for i in range(n):
    mapp.append(int(input()))


def dfs(idx):
    global visit_set

    # 순환구조일 경우 return
    if mapp[idx] == start:
        for i in visit_set:
            result[i] = True
        return

    # 순환구조가 아닐 경우 return
    if mapp[idx] in visit_set:
        return

    # 다음 인덱스 방문처리
    visit_set.add(mapp[idx])
    # 다음 인덱스 dfs
    dfs(mapp[idx])


# dfs 돌리기
start = 0
for i in range(1, n + 1):
    if result[i]:
        continue
    if mapp[i] < i:
        continue
    start = i
    visit_set = set()
    visit_set.add(i)
    dfs(i)

print(result.count(True))
for i in range(len(result)):
    if result[i]:
        print(i)
