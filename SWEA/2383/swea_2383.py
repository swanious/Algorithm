import sys
sys.stdin = open('test.txt','r')

def get_dis(ey, ex, y, x):
    return abs(ey - y) + abs(ex - x)

# 이동중인사람들, 계단높이 
def calc(s_people, height):
    count, waiting = 0, 0
    processing = [] # 내려가는 사람
    while s_people or waiting or processing:

        # 계단을 내려가는 사람의 수가 3명이면 break 아니면 추가
        while waiting:
            if len(processing) == 3:
                break
            processing.append(height)
            waiting -= 1
        
        # 내려가는 사람들의 시간을 -1씩
        for i in range(len(processing)-1, -1, -1):
            processing[i] -= 1
            if processing[i] == 0:
                processing.pop(i)

        # 계단으로 이동중인 사람들의 시간을 -1씩
        for i in range(len(s_people)-1, -1, -1):
            s_people[i] -= 1
            if s_people[i] == 0:
                s_people.pop(i)
                waiting += 1

        count += 1
    return count

def dfs(idx):
    global min_count

    if idx == nums:
        s1_people, s2_people = [], []
        for i in range(nums):
            if check[i]: s1_people.append(p_li[i][0])
            else: s2_people.append(p_li[i][1])

        
        count = max(calc(sorted(s1_people), s_li[0][2]), calc(sorted(s2_people), s_li[1][2]))
        min_count = min(count, min_count)
        return
    
    check[idx] = True
    dfs(idx + 1)
    check[idx] = False
    dfs(idx + 1)
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    nums, min_count = 0, 987654321
    p_li, s_li = [], []

    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 1:
                p_li.append([i, j])
                nums += 1
            elif mapp[i][j] > 1:
                s_li.append([i, j, mapp[i][j]])
    check = [False] * nums

    # [y, x] -> [계단1과의 거리, 계단2와의 거리] 초기화
    for i in range(nums):
        d1 = get_dis(s_li[0][0], s_li[0][1], p_li[i][0], p_li[i][1])
        d2 = get_dis(s_li[1][0], s_li[1][1], p_li[i][0], p_li[i][1])
        p_li[i][0] = d1
        p_li[i][1] = d2
    

    dfs(0) # 조합 구하기
    print("#{} {}".format(tc, min_count + 1)) # 1분 추가