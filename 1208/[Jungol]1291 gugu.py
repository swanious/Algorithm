while True:
    s, e = map(int, input().split())
    if s < 2 or s >= 10 or e < 2 or e >= 10:
        print('INPUT ERROR!')
    else:
        if s > e:
            for i in range(1, 10):
                for j in range(s, e-1, -1):
                    if len(str(j * i)) == 1:
                        print(j, '*', i, '=' + ' ', j * i, end='   ')
                    else:
                        print(j, '*', i, '=', j * i, end='   ')
                print()
            break

        else:
            for i in range(1, 10):
                for j in range(s, e+1):
                    if len(str(j * i)) == 1:
                        print(j, '*', i, '=' + ' ', j * i, end='   ')
                    else:
                        print(j, '*', i, '=', j * i, end='   ')
                print()
            break

'''
정답 형식

4 6
4 * 1 =  4   5 * 1 =  5   6 * 1 =  6   
4 * 2 =  8   5 * 2 = 10   6 * 2 = 12   
4 * 3 = 12   5 * 3 = 15   6 * 3 = 18   
4 * 4 = 16   5 * 4 = 20   6 * 4 = 24   
4 * 5 = 20   5 * 5 = 25   6 * 5 = 30   
4 * 6 = 24   5 * 6 = 30   6 * 6 = 36   
4 * 7 = 28   5 * 7 = 35   6 * 7 = 42   
4 * 8 = 32   5 * 8 = 40   6 * 8 = 48   
4 * 9 = 36   5 * 9 = 45   6 * 9 = 54   
'''