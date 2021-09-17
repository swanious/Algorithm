# 이 문제는 최대값을 구하면 되는 문제이므로, 굳이 배열을 받을 필요없이 바로 계산
n, m = map(int,input().split())

cut_n = int(input())
width = [0]
height = [0]
max_w = 0
max_h = 0
for _ in range(cut_n):
    data = list(map(int, input().split()))
    if data[0] == 0:
        width.append(data[1])
    else:
        height.append(data[1])
width.sort()
width.append(m)
height.sort()
height.append(n)

for i in range(len(width)-1):
    if max_w < width[i+1] - width[i]:
        max_w = width[i+1] - width[i]
for i in range(len(height)-1):
    if max_h < height[i+1] - height[i]:
        max_h = height[i+1] - height[i]
print(max_w * max_h)

