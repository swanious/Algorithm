#https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c
def dfs_comb(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1] + 1, len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret


def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)