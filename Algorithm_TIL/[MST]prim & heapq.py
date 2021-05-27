# 전형적인 prim 알고리즘

def MST_prim():
    # 가중치의 값 초기화
    # 방문 체크할 배열
    # 첫 노드의 값 초기화
    key = [987654321] * (V + 1)
    visited = [False] * (V + 1)
    key[0] = 0
    
    # 모든 간선을 다 가볼 반복문
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        
        # minV, min_idx 찾기
        # key(가중치 배열)에서 작은 값과 그 인덱스(정점)을 저장
        # 방문체크
        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_value = key[i]
                min_idx = i

        visited[min_idx] = True

        # 가중치 값 바꿔주기
        for i in range(V + 1):
            if not visited[i] and adj[min_idx][i] < key[i]:
                key[i] = adj[min_idx][i]

    return sum(key)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    
    # 인접 행렬
    for i in range(E):
        a, b, w = map(int, input().split())
        adj[a][b] = adj[b][a] = w

    print("#{} {}".format(tc, MST_prim()))
##############################################
import heapq  # 힙 큐 이용


def MST_PRIM():
    visited = [False] * (V + 1)

    heap = []  # heapq를 담을 리스트

    # 가중치, 정점(앞이 우선순위로 정렬됨 - 순서 중요)
    heapq.heappush(heap, (0, 0))
    ans = 0

    while heap:
        w, v = heapq.heappop(heap)  # 가중치 정점

        if not visited[v]:
            ans += w  # 힙에서 뽑은 것(최솟 값)을 바로 더해줌
            visited[v] = True

            for idx, weight in adj[v]:  # pop한 정점(v)의 인접리스트를 돌면서 힙에 집어넣음
                if not visited[idx]:
                    heapq.heappush(heap, (weight, idx))


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        a, b, w = map(int, input().split())

        # 정점, 가중치
        adj[a].append((b, w))
        adj[b].append((a, w))

    print("#{} {}".format(tc, MST_prim()))
