import sys

n = int(input())
a = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    a.append(temp)
for i in range(len(a)):
    a[i][0], a[i][1] = a[i][1], a[i][0]
a.sort()

start_v = a[0][0]
result_list = []
result_list.append(a[0])
for i in range(1, len(a)):
    if a[i][1] >= start_v:
        result_list.append(a[i])
        start_v = a[i][0]
print(len(result_list))