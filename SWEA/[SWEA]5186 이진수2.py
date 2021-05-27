'''
3
0.625
0.1
0.125
'''

T = int(input())
for tc in range(1, T + 1):
    n = float(input())
    result = ''
    i = 1
    check = 0
    while True:
        if len(result) >= 13:
            result = 'overflow'
            break

        if n > check + (2 ** -i):
            check += 2 ** -i
            i += 1
            result += '1'

        elif n < check + (2 ** -i):
            i += 1
            result += '0'
            continue

        else:
            result += '1'
            break

    print('#{} {}'.format(tc, result))