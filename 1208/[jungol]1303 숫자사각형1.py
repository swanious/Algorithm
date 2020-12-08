n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        arr[i][j] = num + 1
        num += 1

for i in range(n):
    print(*arr[i])
    
'''
정답
4 6
1 2 3 4 5 6
7 8 9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
'''