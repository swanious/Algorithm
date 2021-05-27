n = int(input())
arr = list(map(int, input().split()))
two = set()
arr.sort()
result = 0
li = []
for i in range(n):
    if arr[i] in two:
        result += 1
        li.append(arr[i])

    for j in range(n):
        if i == j: continue
        if not arr[i] or not arr[j]: continue
        two.add(arr[i] + arr[j])

print(result)
