from itertools import combinations
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test in range(T):

    N = int(input())
    r = N // 2
    s = set(i for i in range(N))
    s1 = list(combinations(s, r))
    s2 = [tuple(s.difference(s1[i])) for i in range(len(s1))]

    mapp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(s1)//2):
        print(s1[i])
        print(s2[i])
    sol = []
    for i in range(len(s1)//2):
        sol1, sol2 = 0, 0
        for j in combinations(s1[i], 2):
            r1, c1 = j[0], j[1]
            sol1 += mapp[r1][c1] + mapp[c1][r1]
        for j in combinations(s2[i], 2):
            r2, c2 = j[0], j[1]
            sol2 += mapp[r2][c2] + mapp[c2][r2]
        sol.append(abs(sol1 - sol2))
    # print("#{} {}".format(test, min(sol)))