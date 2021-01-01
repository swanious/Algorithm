'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''

n = int(input())

# 큰 사각형의 넓이 구하기
arr = []
for i in range(6):
    temp1, temp2 = map(int, input().split())
    arr.append(temp2)

# 면적의 합을 구할 배열
# 각 index를 튜플에 넣을 배열
# 면적의 합이 가장 큰 index
sum_list = []
index_list = []
max_idx = 0

i, j = 0, 1
while i < 6:
    sum_list.append(arr[i] * arr[j])
    i += 1
    j = (j + 1) % 6
    index_list.append((i, j))

max_sqr = max(sum_list)
max_idx = sum_list.index(max(sum_list))

res = max_sqr - sum_list[(max_idx + 3) % 6]
result = res * n

print(result)