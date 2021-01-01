


def perm(k, val):
    global result, minV, maxV
    if k == N:
        if maxV < val:
            maxV = val

        if minV > val:
            minV = val
        result = maxV - minV

    else:
        for i in range(N):
            if OP[0] >= 1:
                OP[0] -= 1
                perm(k + 1, val + NUMS[k + 1])
                OP[0] += 1

            if OP[1] >= 1:
                OP[1] -= 1
                perm(k + 1, val - NUMS[k + 1])
                OP[1] += 1

            if OP[2] >= 1:
                OP[1] -= 1
                perm(k + 1, val * NUMS[k + 1])
                OP[1] += 1

            if OP[3] >= 1:
                OP[1] -= 1
                perm(k + 1, int(val / NUMS[k + 1]))
                OP[1] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())-1
    NUMS = list(map(int, input().split()))
    OP = list(map(int, input().split()))

    result, maxV, minV = 0, 0, 0
    perm(0, 0)
    print(result)