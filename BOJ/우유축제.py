'''
7
0 1 2 0 1 2 0
'''

n = int(input())
milk_list = list(map(int, input().split())) + [-1]
cnt = 0

for i in range(n):
    if milk_list[i] == cnt % 3:
        cnt += 1
print(cnt)
