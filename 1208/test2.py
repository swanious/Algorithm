n = int(input())


def recur(k):
    if n == k:
        print(used)
        return
    else:
        for i in range(1, 7):
            used[k] = i
            recur(k + 1)

used = [0] * n
recur(0)
