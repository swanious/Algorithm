n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), 100 * n
while start < end:
    mid = (start + end) // 2  # 합

    hap = [0] * n
    group = [1] * n
    for i in range(n):
        if i == 0:
            hap[i] = arr[i]
            continue

        hap[i] = hap[i - 1] + arr[i]
        if hap[i] <= mid:
            group[i] = group[i - 1]
        else:
            hap[i] = arr[i]
            group[i] = group[i - 1] + 1

    if group[-1] > m:
        start = mid + 1

    else:
        end = mid

print(start)

ans = [1] * m
result = 0
idx = 0
adn = n - m
for i in range(n):
    if not adn:
        break
    if i == 0:
        result += arr[0]
        continue
    result += arr[i]
    if result <= start:
        ans[idx] += 1
        adn -= 1
    else:
        result = arr[i]
        idx += 1


print(*ans)
