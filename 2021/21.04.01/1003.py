T = int(input())
for _ in range(T):
    n = int(input())
    fibo_list = [0] * (41)
    fibo_list[0] = 0
    fibo_list[1] = 1

    for i in range(2, n + 1):
        fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo_list[n - 1], fibo_list[n])
