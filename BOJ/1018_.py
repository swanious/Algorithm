'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''
'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
'''
# 행, 열
n, m = map(int, input().split())
mapp = []
min_number = []

# 배열 받기
for _ in range(n):
    mapp.append(input())

# 전체 n - 8 + 1 만큼 돌아줘야함
for i in range(n - 7):
    for j in range(m - 7):
        # 색이 틀린 횟수 저장할 값
        # (0, 0) (0, 2)과 같이 행, 열의 인덱스의 합이 짝수일 경우 -> idx1
        # (0, 1) (0, 3)과 같이 홀수일 경우 -> idx2
        idx1 = 0
        idx2 = 0
        # 배열 돌아서 색이 맞지 않는 경우 숫자 올려주기
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if mapp[a][b] != 'W': idx1 += 1
                    if mapp[a][b] != 'B': idx2 += 1
                else:
                    if mapp[a][b] != 'B': idx1 += 1
                    if mapp[a][b] != 'W': idx2 += 1
        # 맞지 않는 횟수 중에서 작은 값 호출
        min_number.append(idx1)
        min_number.append(idx2)
print(min(min_number))

