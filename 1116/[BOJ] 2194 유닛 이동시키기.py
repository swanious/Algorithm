from collections import deque

n, m, a, b, k = map(int, input().split())  # 행 / 열 / 유닛행 / 유닛열 / 장애물 개수
mapp = [[0] * (m + 2) for _ in range(n + 2)]  # 맵을 0으로 초기화

# 가장자리 벽만들기
for i in range(n + 2):  # 행
    mapp[i][0] = 1
    mapp[i][m + 1] = 1
for i in range(m + 1):  # 열
    mapp[0][i] = 1
    mapp[n + 1][i] = 1

# 장애물 좌표 지정
for i in range(k):
    temp1, temp2 = map(int, input().split())
    mapp[temp1][temp2] = 1

# 시작 / 목표 값 저장
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

q = deque()
# 시작 위치 지정
mapp[sy][sx] = 2
q.append((sy, sx, 0))

# 종료 위치 지정
mapp[ey][ex] = 3

# 방향
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 결과 값
cnt = -1

def bfs(y, x, count):
    global cnt

    # 유닛의 크기(테스트 케이스는 2*2)별로 돌면서 4방향 다 갈 수 있는지 체크
    k_cnt = [0] * 4
    for i in range(y, y + a):
        for j in range(x, x + b):
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or ny > n or nx < 0 or nx > m:
                    continue
                if mapp[ny][nx] == 1:
                    continue
                k_cnt[k] += 1

    # 유닛 이동
    # k_cnt[i]가 4일 경우 -> 4방향 모두 움직일 수 있다는 뜻
    for i in range(4):
        if k_cnt[i] == a * b:
            if mapp[y + dy[i]][x + dx[i]] == 2:
                continue
            mapp[y + dy[i]][x + dx[i]] = 2
            q.append((y + dy[i], x + dx[i], count + 1))

while q:
    v = q.popleft()
    if v[0] == ey and v[1] == ex:
        cnt = v[2]
        break
    bfs(v[0], v[1], v[2])
print(cnt)
