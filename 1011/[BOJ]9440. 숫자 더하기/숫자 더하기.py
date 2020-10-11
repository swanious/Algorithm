'''
5 1 2 7 8 9
6 3 4 2 2 2 2
9 0 1 2 3 4 0 1 2 3
0
'''

while 1:
    temp = list(map(int, input().rstrip().split()))
    if len(temp) == 1 and temp[1] == 0:
        break

    n = temp[0]
    arr = temp[1:]


    for i in range()