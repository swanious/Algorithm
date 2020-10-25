from collections import deque
from pprint import pprint
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
G = dict()
for i in range(n):
    G[i] = []
    for j in range(n):
        if arr[i][j] == 1:
            value = G[i]
            value.append(j)
            G[i] = value

q = deque()
for i in range(len(G)):
    q.append(i)
    visit = [0] * len(G)
    while q:
        start = q.popleft()
        for w in G[start]:
            if visit[w]:
                continue
            visit[w] = 1
            arr[i][w] = 1
            q.append(w)

for i in range(n):
    print(*arr[i])

# for m in range(len(G)): # 경유지 기준으로
#     for st in range(len(G)): # 시작점 다 돌려보고
#         for end in range(len(G)): # 도착점 다 돌려봤을 때
#             if arr[st][end] == 0: # 만약 시작점에서 도착점으로 가는 곳이 현재까지는 없는 경우
#                 arr[st][end] = arr[st][m] & arr[m][end] # 가능하다면 갈 수 있다고 판단하여 배열 바꿔줌
# print(arr)