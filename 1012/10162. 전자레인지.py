n = int(input())
a, b, c = 300, 60, 10
ac, bc, cc = 0, 0, 0
flag = True

if n % c != 0:
    flag = False

else:
    if n // a != 0:
        ac = n // a
        n = n % a

    if n // b != 0:
        bc = n // b
        n = n % b

    if n // c != 0:
        cc = n // c
        n = n % c

if flag == True:
    print(ac, bc, cc)
else:
    print(-1)
