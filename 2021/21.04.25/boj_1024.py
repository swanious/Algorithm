'''
18 2
'''

n, l = map(int, input().split())

result = []
for i in range(l, 101):
    # 홀
    if i % 2:
        if not n % i:
            mean = n // i
            mean_left = mean - (i - 1) // 2
            if mean_left < 0: break  # 평균의 왼쪽값이 음수이면 break
            mean_right = mean + (i - 1) // 2
            result = range(mean_left, mean_right + 1)
            break
    # 짝
    else:
        mean = n / i
        # 짝수일때는 정수.5의 값이 나와야한다.
        if mean - int(mean) == 0.5:
            mean_left = int(mean) - (i // 2 - 1)
            if mean_left < 0: break
            mean_right = int(mean + 0.5) + (i // 2 - 1)
            result = range(mean_left, mean_right + 1)
            break

if result:
    print(*result)
else:
    print(-1)
