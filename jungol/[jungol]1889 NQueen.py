# def dfs(arr, n):
#     global ans
#
#     if len(arr) == n:  # 정답 배열(arr)의 길이가 n과 같아지면 ans를 1올리고 return
#         ans += 1
#         return 0
#
#     candidate = list(range(n)) # 0부터 n-1까지 후보 배열을 만든다.
#     for i in range(len(arr)):
#         if arr[i] in candidate:
#             candidate.remove(arr[i])
#
#         distance = len(arr) - i
#         if arr[i] + distance in candidate:  # 같은 대각선 상에 있으면 후보 삭제
#             candidate.remove(arr[i] + distance)
#         if arr[i] - distance in candidate:  # 같은 대각선 상에 있으면 후보 삭제
#             candidate.remove(arr[i] - distance)
#
#     if candidate != []:
#         for i in candidate:
#             arr.append(i)  # 후보의 요소를 정답 배열의 다음 요소로 추가
#             dfs(arr, n)  # 재귀
#             arr.pop()
#
#     else:
#         return 0
# ans = 0
# n = int(input())
# for i in range(n):
#     dfs([i], n);
# print(ans)

def possible(idx, c):
    for i in range(idx):
        # 행과 열의 차이가 같다면
        if idx - i == abs(c - map_list[i]): return True
    return False


def dfs(idx):
    if idx == N:
        global answer
        answer += 1
        return
    for i in range(N):
        # 이미 사용한 열이라면 넘어감
        if visit[i]: continue
        # 대각선이 겹친다면 넘어감
        if possible(idx, i): continue
        visit[i] = 1
        map_list[idx] = i
        dfs(idx + 1)
        visit[i] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    map_list = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print('#{} {}'.format(t, answer))