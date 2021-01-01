# 비트연산 powerset
for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())

    score, calo = [], []
    for i in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calo.append(c)

    ans = 0
    # 비트연산을 통해 모든 부분집합 구하기
    for i in range(1 << N):
        sum_score = 0
        sum_calo = 0
        for j in range(N):
            if i & (1 << j):
                sum_score += score[j]
                sum_calo += calo[j]

        if sum_calo <= L:
            ans = max(ans, sum_score)
    print("#{} {}".format(tc, ans))


#####################################################

# 재귀 형식
def cook(idx):
    global ans

    if idx >= N:
        sum_score = 0
        sum_calo = 0

        for i in range(N):
            if sel[i]:
                sum_score += score[i]
                sum_calo += calo[i]
        if sum_calo <= L:
            ans = max(ans, sum_score)
        return

    # 재료를 뽑고가고
    sel[idx] = True
    cook(idx + 1)
    # 재료를 안뽑고가고
    sel[idx] = False
    cook(idx + 1)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())

    score, calo = [], []
    for i in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calo.append(c)

    ans = 0
    sel = [False] * N
    cook(0)
    print(ans)


###################################################
# 백트래킹
def cook(idx, sum_score, sum_calo):
    global ans

    if sum_calo > L:
        return
    # 여기서 ans를 갱신해도 좋음(위에서 Limit를 넘은 재료는 걸러줬으니)

    if idx == N:
        if sum_score > ans:
            ans = sum_score
        return

    # 재료를 뽑고 가고
    cook(idx + 1, sum_score + score[idx], sum_calo+calo[idx])
    # 재료를 안뽑고 가고
    cook(idx + 1, sum_score, sum_calo)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())

    score, calo = [], []
    for i in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calo.append(c)

    ans = 0
    cook(0, 0, 0)
