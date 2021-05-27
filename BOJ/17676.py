num = int(input())

DP = [4] * 50000
result = 0

# 제곱수들에 1을 채워넣음
for i in range(1, len(DP)):
    if i ** 2 > 50000:
        break
    DP[pow(i, 2)] = 1

# 만약 num이 제곱수이면 1을 반환
if DP[num] == 1:
    print(DP[num])

else:
    for i in range(1, num + 1):
        if DP[i] == 1:
            continue

        for j in range(1, num + 1):
            temp = i - j ** 2
            if temp < 0:
                break

            if DP[temp] == 1:
                DP[i] = 2
                break

            if DP[temp] == 2:
                DP[i] = min(DP[i], 3)

    print(DP[num])
