a = "ASADADAS"
n = len(a)


def run(t):
    if t == n:
        print()
        return
    print(a[t], end='')
    run(t + 1)
    print(a[t], end='')

run(0)