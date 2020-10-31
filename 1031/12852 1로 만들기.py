'''
bfs로 풀어본 결과 경로를 구하기가 힘들어 포기한 후, 1에서 목푯 값으로 역추적하는 DP방식을 채택
'''

n = int(input())
arr = [[0, []] for _ in range(n + 1)]  # 횟수, 경로 찾기
arr[1][0] = 0
arr[1][1] = [1]
for i in range(2, n + 1):
    # 1 빼기
    arr[i][0] = arr[i - 1][0] + 1
    arr[i][1] = arr[i - 1][1] + [i]

    # 2 나누기
    # 최솟값을 찾아야하므로 2로 나누어떨어지고, DP[i][0]가 2로 나눈 횟수의 값보다 크면 교체해준다.
    if i % 2 == 0 and arr[i][0] > arr[i // 2][0] + 1:
        arr[i][0] = arr[i // 2][0] + 1
        arr[i][1] = arr[i // 2][1] + [i]

    # 3 나누기
    # 최솟값을 찾아야하므로 3로 나누어떨어지고, DP[i][0]가 3로 나눈 횟수의 값보다 크면 교체해준다.
    if i % 3 == 0 and arr[i][0] > arr[i // 3][0] + 1:
        arr[i][0] = arr[i // 3][0] + 1
        arr[i][1] = arr[i // 3][1] + [i]

print(arr[n][0])
arr[n][1].reverse()
for i in arr[n][1]:
    print(i, end=' ')
