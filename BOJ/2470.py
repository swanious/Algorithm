n = int(input())

solution = sorted(list(map(int, input().split())))
min_value = 99999999999
result = [0, 0]
for i in range(n):
    find = -solution[i]
    start, end = 0, n - 1
    while start < end:
        mid = (start + end) // 2
        if solution[mid] == find:
            result[0] = solution[i]
            result[1] = solution[mid]
            break

        elif solution[mid] < find:
            start = mid + 1

        else:
            end = mid

    if start != 0 and start-1 != i:  # 똑같은 인덱스가 아닌 왼쪽값을 더해서 확인
        hap = abs(solution[start - 1] + solution[i])
        if min_value > hap:
            min_value = hap
            result[0] = solution[i]
            result[1] = solution[start - 1]

    # 똑같은 인덱스가 아닌 값만
    if start != i:
        hap = abs(solution[start] + solution[i])  # 원래 값(우측값)을 더해서 확인
        if min_value > hap:
            min_value = hap
            result[0] = solution[i]
            result[1] = solution[start]
result = [min(result), max(result)]
print(*result)