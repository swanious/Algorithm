n = int(input())
buildings = []
ans = [0] * (n + 1)
tmp = 0
for i in range(1, n + 1):
    tmp, idx = int(input()), i
    if buildings == []:
        buildings.append((tmp, idx))
        continue

    if tmp > buildings[-1][0]:
        while True:
            # buildings배열이 비어있으면 break
            if not buildings: break

            # buildings배열의 top이 tmp보다 크면 break
            if buildings[-1][0] > tmp: break
            height, idx = buildings.pop()
            ans[idx] = i
        if len(buildings) == 1: break
        buildings.append((tmp, idx))
    else:
        buildings.append((tmp, idx))

for i in range(1, n+1):
    print(ans[i])