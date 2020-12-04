'''
2
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2
'''

from collections import deque


def push():
    if S == 'up':
        # 열 우선순회
        for i in range(N):
            q = deque()
            for j in range(N):
                if arr[j][i]:
                    q.append(arr[j][i])
                    arr[j][i] = 0
            # 가장 위부터 채워 나가기
            idx = 0
            while q:
                if len(q) > 1:
                    A, B = q.popleft(), q.popleft()
                    if A == B:
                        arr[idx][i] = A + B
                    else:
                        arr[idx][i] = A
                        q.appendleft(B)
                    idx += 1
                else:
                    arr[idx][i] = q.popleft()


    elif S == 'down':
        # 열 우선순회
        for i in range(N):
            q = deque()
            for j in range(N - 1, -1, -1):
                if arr[j][i]:
                    q.append(arr[j][i])
                    arr[j][i] = 0
            # 가장 위부터 채워 나가기
            idx = N - 1
            while q:
                if len(q) > 1:
                    A, B = q.popleft(), q.popleft()
                    if A == B:
                        arr[idx][i] = A + B
                    else:
                        arr[idx][i] = A
                        q.appendleft(B)
                    idx -= 1
                else:
                    arr[idx][i] = q.popleft()


    elif S == 'left':
        # 열 우선순회
        for i in range(N):
            q = deque()
            for j in range(N):
                if arr[i][j]:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            # 가장 위부터 채워 나가기
            idx = 0
            while q:
                if len(q) > 1:
                    A, B = q.popleft(), q.popleft()
                    if A == B:
                        arr[i][idx] = A + B
                    else:
                        arr[i][idx] = A
                        q.appendleft(B)
                    idx += 1
                else:
                    arr[i][idx] = q.popleft()

    else:
        # 열 우선순회
        for i in range(N):
            q = deque()
            for j in range(N - 1, -1, -1):
                if arr[i][j]:
                    q.appendleft(arr[i][j])
                    arr[i][j] = 0
            # 가장 위부터 채워 나가기
            idx = N - 1
            while q:
                if len(q) > 1:
                    A, B = q.popleft(), q.popleft()
                    if A == B:
                        arr[i][idx] = A + B
                    else:
                        arr[i][idx] = A
                        q.appendleft(B)
                    idx -= 1
                else:
                    arr[i][idx] = q.popleft()


for tc in range(1, int(input()) + 1):
    N, S = input().split()
    N = int(N)

    arr = [list(map(int, input().split())) for _ in range(N)]

    push()

    print("#{}".format(tc))
    for i in range(N):
        print(*arr[i])
