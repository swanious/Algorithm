import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 이분탐색으로 차이를 구한다.
start, end = 0, 9999
while start < end:
    mid = (start + end) // 2  # 차이
    # 최솟값, 최대값, 그룹
    minV = [99999] * n
    maxV = [0] * n
    group = [1] * n
    for i in range(n):
        if i == 0:
            minV[i] = arr[i]
            maxV[i] = arr[i]
            continue

        minV[i] = min(minV[i - 1], arr[i])
        maxV[i] = max(maxV[i - 1], arr[i])
        if maxV[i] - minV[i] <= mid:
            group[i] = group[i - 1]
        else:
            group[i] = group[i - 1] + 1
            minV[i] = arr[i]
            maxV[i] = arr[i]
    if m >= group[-1]:
        end = mid
    else:
        start = mid + 1

# 반복문이 끝나면 start가 최적해가 나온다.
print(start)
