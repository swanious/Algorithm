# import sys
#
# n = int(input())
# A = [0] * n
# ans = 0
#
# dy = [1, 1]
# dx = [1, -1]
#
# def check(y, x):
#     # 직선과 대각선 확인
#     for qy in range(y):
#         qx = A[qy]
#         # 직선 확인
#         if qx == x:
#             return False
#
#         # 대각선 확인
#         if (qx - x) and abs((qy - y) / (qx - x)) == 1:
#             return False
#
#
#         # for d in range(2):
#         #     ny, nx = qy, qx
#         #
#         #     while ny != y:
#         #         ny, nx = ny + dy[d], nx + dx[d]
#         #
#         #     if nx == x:
#         #         return False
#
#     return True
#
#
# def dfs(y):
#     if y == n:
#         global ans
#         ans += 1
#         return
#
#     for x in range(n):
#         if check(y, x):
#             A[y] = x
#             dfs(y + 1)
#
# dfs(0)
# print(ans)

n = int(input())
Qx = [-1] * n
ans = 0

iy = [1, 1]
ix = [1, -1]


def dfs(y):
    global ans

    if y == n:
        ans += 1
        return

    for x in range(n):
        if x not in Qx:
            # d = 0
            # # 대각선 확인
            # for qy in range(y):  # 0 ~ y - 1
            #     qx = Qx[qy]
            #     for i in range(2):
            #         dy, dx = qy, qx
            #         while dy != y:
            #             dy, dx = dy + iy[i], dx + ix[i]
            #
            #         if x != dx:
            #             d += 1
            #
            # # 2개의 대각선이 모두 확인되면 선택
            # if d == 2 * y:
            #     Qx[y] = x
            #     dfs(y + 1)
            #     Qx[y] = -1

            d = 0
            # 대각선 확인
            for qy in range(y):  # 0 ~ y - 1
                qx = Qx[qy]
                for i in range(2):
                    dy, dx = qy, qx
                    while dy != y:
                        dy, dx = dy + iy[i], dx + ix[i]

                    if x != dx:
                        d += 1

            # 2개의 대각선이 모두 확인되면 선택
            if d == 2 * y:
                Qx[y] = x
                dfs(y + 1)
                Qx[y] = -1


dfs(0)
print(ans)
