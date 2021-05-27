from collections import deque

'''
110
1000

101
111
'''
start_number = int(input())
end_number = int(input())
start_sum = 0
end_sum = 0
i = 0
# 시작 값
while start_number:
    # num을 10으로 나눈 나머지(비트 형태)를 현재의 자리(i)만큼 쉬프트 연산한 값을 곱해준다.
    start_sum += (start_number % 10) * (1 << i)
    start_number //= 10
    i += 1

i = 0
# 목표 값
while end_number:
    # num을 10으로 나눈 나머지(비트 형태)를 현재의 자리(i)만큼 쉬프트 연산한 값을 곱해준다.
    end_sum += (end_number % 10) * (1 << i)
    end_number //= 10
    i += 1

# bfs를 돌려서 바꿀 수 있는 경우를 전부 바꿔서 확인하고 맞으면 정지(목표값 찾으면)
# q에 정수와 거리값을 넣어준다.
visited = [False] * 10000
result = 0
q = deque()
visited[start_sum] = True
q.append((start_sum, 0))
while q:
    b = q.popleft()
    if b[0] == end_sum:
        result = b[1]
        break
    # 첫번째 숫자의 비트 찾기
    idx = 0
    while b[0] >= (1 << idx):
        idx += 1
    idx -= 1

    # 조건 1
    new_b = 0
    for i in range(idx-1, -1, -1):
        if (b[0] & (1 << i)) > 0:
            new_b = b[0] - (1 << i)

        else:
            new_b = b[0] + (1 << i)

        if new_b < 0 or new_b > 5000:
            continue

        if visited[new_b]:
            continue

        visited[new_b] = True
        q.append((new_b, b[1] + 1))

    # 조건 2, 3
    for i in range(2):
        # 조건 2
        if i == 0 and b[0] < 4999:
            new_b = b[0] + 1

        # 조건 3
        elif i == 1 and b[0] != 0:
            new_b = b[0] - 1

        else:
            continue

        if visited[new_b]:
            continue

        visited[new_b] = True
        q.append((new_b, b[1] + 1))

print(result)
