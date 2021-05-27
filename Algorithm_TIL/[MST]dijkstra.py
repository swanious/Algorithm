# SWEA Ad - 최소 이동 거리

def dijkstra():
    dist = [987654321] * (v + 1)

    visited = [False] * (v + 1)

    dist[0] = 0

    for _ in range(v + 1):
        min_idx = -1
        min_value = 987654321

        # 최소값을 가진 인덱스 찾기
        # 신병 정점 찾기
        for i in range(v + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = True

        # 신병 간선 업데이트
        for i in range(v + 1):
            if not visited[i] and dist[i] > dist[min_idx] + adj[min_idx][i]:
                dist[i] = dist[min_idx] + adj[min_idx][i]
    return dist

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    adj = [[987654321] * (v + 1) for _ in range(v + 1)]

    for i in range(e):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w
    print(adj)
    print(dijkstra())
#################################################
# dijkstra - heap ver.
# import heapq
#
#
# def dijstra_heap():
#     dist = [987654321] * (v + 1)
#     visited = [False] * (v + 1)
#
#     heap = []
#     dist[0] = 0
#
#     # 가중치 정점(순서 중요)
#     heapq.heappush(heap, (0, 0))
#
#     while heap:
#         w, v = heapq.heappop(heap)
#
#         if not visited[v]:
#             visited[v] = True
#             dist[v] = w
#
#             # 전체 순회를 하면서 경유한 경우가 원래의 값보다 작으면, 작은 값으로 교체
#             for i in range(v + 1):
#                 if not visited[i] and dist[i] > dist[v] + adj[v][i]:
#                     heapq.heappush(heap, (dist[v] + adj[v][i], i))
#
#
# for tc in range(1, int(input()) + 1):
#     v, e = map(int, input().split())
#     adj = [[987654321] * (v + 1) for _ in range(v + 1)]
#
#     for i in range(e):
#         st, ed, w = map(int, input().split())
#         adj[st][ed] = w
