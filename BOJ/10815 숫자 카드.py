from sys import stdin

n = int(input())
target = list(map(int, stdin.readline().rstrip().split()))
m = int(input())
arr = list(map(int, stdin.readline().rstrip().split()))

target_dic = dict()
for i in target:
    target_dic[i] = True

for i in arr:
    if target_dic.get(i) == True:
        print(1, end=' ')
    else:
        print(0, end=' ')