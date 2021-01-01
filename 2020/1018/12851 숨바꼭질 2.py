from collections import deque

n, m = map(int, input().split())
q = deque()
visited = [False] * 100001

cnt = 0  # 같은 층에 목표값의 개수
save = 100001  # 찾은 값의 계층을 저장할 변수

q.append([n, 0])
temp = 0
while q:
    v = q.popleft()
    if v[0] == m:
        save = v[1]
        cnt += 1
        continue

    if v[1] > save:
        break

    visited[v[0]] = True
    for i in range(3):
        if i == 0:
            temp = v[0] - 1
        elif i == 1:
            temp = v[0] + 1
        elif i == 2:
            temp = v[0] * 2
        if temp < 0 or temp > 100000:
            continue
        if visited[temp] == True:
            continue

        # 위는 v[1]의 값이 오르는 것이 아니다. 꼭 알아두자 !
        # for문이 한번 돌때마다 기존의 v[1]에 1을 올려준 상태를 append 할뿐이다.(값이 증가한게 아니다.)
        # bfs돌면서 v[1]값을 올려줘야하므로 전역변수를 따로 설정해서 돌려주면 안된다.
        q.append([temp, v[1] + 1])

print(save)
print(cnt)
