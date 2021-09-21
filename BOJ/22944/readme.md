# 22944 죽음의 비

> [문제 링크](https://www.acmicpc.net/problem/22944)

## 설계

1. 시작, 끝, 우산들(Array)의 좌표를 변수에 저장한다.
2. 우산 위치 배열을 돌면서 우산의 경로를 바꿔보면서 재귀를 돈다.(순열)
3. 조건은 크게 두가지로 `1.현재의 체력으로 바로 갈 수 있는 경우`, `2. 새로운 우산을 가지고 가야하는 경우`

   - 1번의 경우 재귀 종료조건으로 현재의 위치에서 종료지점으로 바로 갈 수 있는 경우 result를 거리로 반환한다.(이전에 더 적게 갈 수 있었으면 그게 답)
   - 2번의 경우 우산의 위치를 바꿔가며 재귀를 수행한다.
     - 이미 갔거나 거리가 죽을 위기면 pass
     - 우산내구도가 거리보다 작으면 일정분 체력을 깎고 재귀수행
     - 우산내구도가 더 높으면 새로운 내구도, 기존체력으로 재귀수행

4. 답이 기존에 초기화해둔 값이면 -1, 아니면 result 반환

## 나의 코드

```python
import sys

input = sys.stdin.readline

n, h, d = map(int, input().split()) # 배열크기, 체력, 우산내구도
mapp = [input() for _ in range(n)]

result = sys.maxsize
sy, sx = 0, 0
ey, ex = 0, 0
u_list = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 'S':
            sy, sx = i, j
        elif mapp[i][j] == 'E':
            ey, ex = i, j
        elif mapp[i][j] == 'U':
            u_list.append((i, j))

visit = [False] * len(u_list)

def get_distance(ey, ex, y, x):
    return abs(ey - y) + abs(ex - x)

def dfs(y, x, life, shield, count):
    global result

    # 1.
    if get_distance(ey, ex, y, x) <= life + shield:
        result = min(result, count + get_distance(ey, ex, y, x))
        return

    # 2.
    for i in range(len(u_list)):
        uy, ux = u_list[i]
        dis = get_distance(uy, ux, y, x)
        if life + shield <= dis - 1 or visit[i]:
            continue

        if shield < dis:
            visit[i] = True
            dfs(uy, ux, life - (dis - shield), d, count + dis)
            visit[i] = False

        else:
            visit[i] = True
            dfs(uy, ux, life, d, count + dis)
            visit[i] = False

dfs(sy, sx, h, 0, 0)
print(-1 if result == sys.maxsize else result)
```

## 후기

- 시작지점, 종료지점, 우산위치 세 개의 위치값에 집중해서 조건에 따른 재귀를 수행했다.
