n = int(input())
ans = 0
oxs = []
for i in range(n):
    tmp = int(input())
    if oxs == []:
        oxs.append(tmp)
        continue

    if oxs[0] < tmp:
        oxs = []
        oxs.append(tmp)
        continue

    elif oxs[-1] <= tmp:
        ans += 1
        oxs.pop()
        oxs.append(tmp)

    elif oxs[-1] > tmp:
        ans = ans + len(oxs)
        oxs.append(tmp)

print(ans)