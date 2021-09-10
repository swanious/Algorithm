# 그래프의 최단거리를 찾기 위해서 bfs를 활용한다.
# 방문체크배열 visit과 거리를 담아둘 distance를 초기화한다.
# 가장 멀리 떨어진 노드는 bfs가 제일 처음 방문한 곳에 [이전노드의 거리 + 1]을 더해주고 다시방문하지 않으면된다.
from collections import deque

def solution(n, edge):
    visit = [False] * (n + 1)
    distance = [0] * (n + 1)
    G = [[] for _ in range(n + 1)]
    for node in edge:
        G[node[0]].append(node[1])
        G[node[1]].append(node[0])
        
    
    visit[1] = True
    q = deque()
    q.append(1)
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                distance[w] = distance[v] + 1
                q.append(w)
    
    return distance.count(max(distance))