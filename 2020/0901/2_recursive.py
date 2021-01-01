#https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c

def comb(lst, n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


def perm(lst, n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret