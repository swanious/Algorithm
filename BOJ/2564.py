'''
10 5
3
1 4
3 2
2 8
2 3
'''
w, h = map(int, input().split())
n = int(input())
store_li = []
for i in range(n+1):
    store_li.append(list(map(int, input().split())))

li = []
result = []
my_dis = 0

# 상점의 거리 리스트
for i in range(n+1):
    if store_li[i][0] == 1: li.append(store_li[i][1])
    elif store_li[i][0] == 2: li.append((2 * w) + h - store_li[i][1])
    elif store_li[i][0] == 3: li.append((2 * w) + (2 * h) - store_li[i][1])
    else: li.append(w + store_li[i][1])

length = (2 * w) + (2 * h)
for i in range(len(li)-1):
    result.append(min(abs(li[i] - li[-1]), length - abs(li[i] - li[-1])))
print(sum(result))