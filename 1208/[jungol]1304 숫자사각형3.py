n = int(input())
arr = [[0] * n for _ in range(n)]
num = 0
for i in range(n):
    for j in range(n):
        arr[j][i] = num + 1
        num += 1
for i in range(n):
    print(*arr[i])

'''
정답
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25
'''