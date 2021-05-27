import sys

sys.stdin = open("input.txt")

for tc in range(1, 11):
    n = int(input())
    b_li = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(b_li) - 2):
        if b_li[i] <= b_li[i - 1] or b_li[i] <= b_li[i + 1] or b_li[i] == 0:
            continue

        elif b_li[i] <= b_li[i - 2] or b_li[i] <= b_li[i + 2] or b_li[i] == 0:
            continue

        # 
        else:
            if b_li[i - 1] >= b_li[i - 2] and b_li[i - 1] >= b_li[i + 1] and b_li[i - 1] >= b_li[i + 2]:
                cnt += b_li[i] - b_li[i - 1]
            elif b_li[i - 2] >= b_li[i - 1] and b_li[i - 2] >= b_li[i + 1] and b_li[i - 2] >= b_li[i + 2]:
                cnt += b_li[i] - b_li[i - 2]
            elif b_li[i + 1] >= b_li[i - 2] and b_li[i + 1] >= b_li[i - 1] and b_li[i + 1] >= b_li[i + 2]:
                cnt += b_li[i] - b_li[i + 1]
            elif b_li[i + 2] >= b_li[i - 2] and b_li[i + 2] >= b_li[i - 1] and b_li[i + 2] >= b_li[i + 1]:
                cnt += b_li[i] - b_li[i + 2]


    print("#{} {}".format(tc, cnt))
