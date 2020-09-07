import sys

sys.stdin = open("input.txt")


def rotation(nums):
    tmp = [[''] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            # 회전하는 함수
            tmp[j][n - 1 - i] = nums[i][j]
    return tmp

def result(nums, col):
    for i in range(n):
        for j in range(n):
            ans[i][col] += nums[i][j]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    # 90, 180, 270 각각 3개
    ans = [[''] * 3 for _ in range(n)]

    for i in range(3):
        arr = rotation(arr)
        result(arr, i)

    print("#{}".format(tc), end=' ')
    for i in range(n):
        for j in range(3):
            print(ans[i][j], end=' ')
        print()
