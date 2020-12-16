drug = [[0]*31 for _ in range(31)]
drug[0][0] = 1
for w in range(31):
    for h in range(31-w):
        if w == h == 0:
            drug[w][h] = 1
            continue
        whole = 0
        half = 0
        if w > 0:
            whole = drug[w-1][h+1]
        if h > 0:
            half = drug[w][h-1]
        drug[w][h] = whole + half

while True:
    n = int(input())
    if not n:
        break
    print(drug[n][0])
