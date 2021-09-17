n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    mapp[i][0] = min(mapp[i-1][1], mapp[i-1][2]) + mapp[i][0]
    mapp[i][1] = min(mapp[i-1][0], mapp[i-1][2]) + mapp[i][1]
    mapp[i][2] = min(mapp[i-1][0], mapp[i-1][1]) + mapp[i][2]
print(min(mapp[n-1][0], mapp[n-1][1], mapp[n-1][2]))