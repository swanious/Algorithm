# 왼쪽값? 윗쪽갑? 왼쪽위 + 1(같은경우) 중에서 max 고르기
a, b = list(input()), list(input())
DP = [[[0, 0, 0] for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]


def first_value(x):
    return x[0]


for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        temp = [DP[i - 1][j - 1][0], i, j]
        if a[j - 1] == b[i - 1]:
            temp[0] += 1
        DP[i][j] = [k for k in max(DP[i][j - 1], DP[i - 1][j], temp, key=first_value)]

print(DP[len(b)][len(a)][0])
if DP[len(b)][len(a)]:
    i = DP[len(b)][len(a)][1]
    j = DP[len(b)][len(a)][2]
    result_list = []
    while DP[i][j][0]:
        result_list += b[DP[i][j][1] - 1]
        i, j = DP[i - 1][j - 1][1], DP[i - 1][j - 1][2]
    print(''.join(result_list[::-1]))

# A,B=input(),input()
# dp=['']*len(B)
#
# for i in range(len(A)):
#     max_dp=''
#     for j in range(len(B)):
#         if len(max_dp) < len(dp[j]):
#             max_dp=dp[j]
#         elif A[i] == B[j]:
#             dp[j]=max_dp+B[j]
#
# # 가장 큰 값 찾기
# ans=''
# for s in dp:
#     if len(ans) < len(s):
#         ans=s
#
# print(len(ans))
# if len(ans):
#     print(ans)