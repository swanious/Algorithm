x, a, b, c, d = map(int, input().split())

# result가 들어차는 순간 답 반영
result = False
turn = False

while a >= 0:
    pick_a = x - a
    if pick_a <= 0:
        result = [x, 0, 0, 0]
        break

    # 빼서 확인
    if pick_a % 5:
        a -= 1
        continue

    _b = b
    while _b >= 0:
        pick_b = pick_a - (_b * 5)
        if pick_b <= 0:
            result = [a, pick_a // 5, 0, 0]
            break

        _c = c
        signal = False
        while _c >= 0:
            pick_c = pick_b - (_c * 10)
            if pick_c <= 0 and not pick_b % 10:
                result = [a, _b, pick_b // 10, 0]
                break

            if pick_c > 0 and not pick_c % 25 and pick_c // 25 <= d and not signal:
                if result:
                    sum_result = sum(result)
                    if sum_result >= sum([a, _b, _c, pick_c // 25]):
                        _c -= 1
                        continue
                result = [a, _b, _c, pick_c // 25]

                signal = True
            _c -= 1

        if result:
            if not turn:
                turn = True
                _b -= 1
                continue
            break
        _b -= 1

    if result:
        break
    a -= 1

if result:
    print(*result)
else:
    print("0 0 0 0")
