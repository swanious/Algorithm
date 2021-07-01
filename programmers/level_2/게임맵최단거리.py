from collections import deque

def solution(maps):
    answer = 0
    # 행/열 길이
    n, m = len(maps), len(maps[0])
    
    # 방향
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
    
    # 방문 배열
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    
    # queue 생성
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        y, x, cnt = q.popleft()
        # 도착지에 도착했으면 break
        if y == n-1 and x == m-1:
            answer = cnt
            break
            
        for i in range(4):
            # 클론 생성 !
            ny, nx = y + dy[i], x + dx[i]
            # 1. 사방 체크하고,
            if ny >= 0 and ny < n and nx >= 0 and nx < m:
                # 2. 장애물/방문체크 후 갈 수 있으면,
                if not visit[ny][nx] and maps[ny][nx]:
                    # 3. 방명록 쓰고, 큐에 넣고
                    visit[ny][nx] = True
                    q.append((ny, nx, cnt + 1))
    
    # 도착지에 못갔으면 -1 반환하고, 아니면 답 반환
    if not visit[n-1][m-1]:
        return -1
    return answer