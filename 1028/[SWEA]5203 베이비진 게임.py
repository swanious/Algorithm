'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''

# 카드를 뽑을 때마다 비교할 함수
def babygin(arr):
    for i in range(len(arr) - 2):
        if arr[i] >= 1 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
            return 1

    for i in range(len(arr)):
        if arr[i] >= 3:
            return 1


for tc in range(1, int(input()) + 1):
    game = list(map(int, input().split()))

    cntA = [0] * 10
    cntB = [0] * 10

    # 2장씩 미리 뽑기(3장 이상부터 baby gin 판별 가능함)
    for i in range(2):
        cntA[game[i * 2]] += 1
        cntB[game[i * 2 + 1]] += 1

    result = 0
    i = 4
    while i < 12:
        if i == 12:
            result = 0

        cntA[game[i]] += 1
        a = babygin(cntA)
        if a == 1:
            result = 1
            break

        cntB[game[i + 1]] += 1
        b = babygin(cntB)
        if b == 1:
            result = 2
            break

        i += 2

    print('#{} {}'.format(tc, result))