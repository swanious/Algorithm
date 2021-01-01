from collections import deque

n = int(input())

q = deque([(1, 0)])

# 방문 체크를 딕셔너리로 처리하면 훨씬 깔끔하다.
visited = dict()

# 현재 화면의 이모티콘 갯수, 복사한 이모티콘 갯수
visited[(1, 0)] = 0
while q:
    v, c = q.popleft()
    if v == n:
        print(visited[(v, c)])
        break

    if (v, v) not in visited and 1 <= v < 2001:
        visited[(v, v)] = visited[(v, c)] + 1
        q.append((v, v))
    if (v - 1, c) not in visited and 1 <= v-1:
        visited[(v - 1, c)] = visited[(v, c)] + 1
        q.append((v - 1, c))
    if (v + c, c) not in visited and 1 <= v+c < 2001:
        visited[(v + c, c)] = visited[(v, c)] + 1
        q.append((v + c, c))