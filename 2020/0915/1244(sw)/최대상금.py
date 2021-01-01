import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    temp, n = map(int, input().split())
    num_li = (list(map(int, str(temp))))

    max_num = 0
    # 숫자를 돌면서 가장 큰 값 맨앞에거랑 바꿈
    # 없을 경우
    # 인덱스 옮김 +1
    i = 0
    first_num = num_li[0]
    for i in range(1, len(num_li)):
        max_num < num_li[i]
        max_num = num_li[i]
    if first_num <= max_num:
        num_li[0], num_li[num_li.index(max_num)] = num_li[num_li.index(max_num)], num_li[0]
    else: