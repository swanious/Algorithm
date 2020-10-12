'''
5 1 2 7 8 9
6 3 4 2 2 2 2
9 0 1 2 3 4 0 1 2 3
0
'''

while 1:
    temp = list(map(int, input().rstrip().split()))
    if temp[0] == 0:
        break

    n = temp[0]
    arr = temp[1:]

    a_list = []
    b_list = []
    arr.sort()

    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        else:
            a_list.append(arr.pop(i))
            break

    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        else:
            b_list.append(arr.pop(i))
            break

    for i in range(len(arr)):
        if i % 2 == 0:
            a_list.append(arr[i])
        else:
            b_list.append(arr[i])

    res1 = ''
    res2 = ''
    for i in a_list:
        res1 += str(i)
    for i in b_list:
        res2 += str(i)

    print(int(res1) + int(res2))