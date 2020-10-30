import sys

sys.stdin=open('1244.txt')

def solveR(numL, n):
    global maxVal

    num = int(''.join(numL))

    if num == possible and (K - n) % 2 == 0  : # 바꿀 횟수가 짝수이면 탈출
        maxVal = possible
        return

    if n == K:
        if num > maxVal :
            maxVal = num

    else:
        for i in range(len(ARR) - 1 ):
            for j in range(1, len(numL)):
                numL[i], numL[j] = numL[j], numL[i]
                solveR(numL, n+1)
                if maxVal == possible  : return # 찾는 도중에 값을 찾으면 탈출
                numL[i], numL[j] = numL[j], numL[i]

T = int(input())
for tc in range(1, T+1):
    l1, l2 = input().split()
    ARR = list(l1)
    K = int(l2)

    possible = int(''.join(sorted(ARR, reverse=True))) # 역순으로 sorted -> str -> int
    maxVal = 0
    solveR(ARR, 0)

    print('#{} {}' .format(tc ,maxVal))