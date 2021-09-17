from itertools import combinations

'''
35 15 10
'''


def combination(x, y, z, count):
    comb = []
    tmp = list(combinations([x, y, z], 2))
    if count > 10:
        return

    for i in range(3):
        comb.append(sorted([tmp[i][0], tmp[i][1]]))


    calculate(comb[0][0], comb[0][1], z, count)
    calculate(comb[1][0], comb[1][1], y, count)
    calculate(comb[2][0], comb[2][1], x, count)


def calculate(x, y, z, count):
    global ans
    if x == y:
        return
    y = y - x
    x = 2 * x
    if x == y == z:
        ans = 1
        return
    else:
        combination(x, y, z, count + 1)


ans = 0
cnt = 0
a, b, c = map(int, input().split())
combination(a, b, c, 0)
if a == b == c:
    print(1)
else:
    print(ans)
