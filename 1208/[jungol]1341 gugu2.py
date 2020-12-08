while True:
    s, e = map(int, input().split())
    if s < 2 or s >= 10 or e < 2 or e >= 10:
        print('INPUT ERROR!')
    else:
        if s > e:
            for i in range(s, e-1, -1):
                for j in range(1, 10):
                    if j % 3 == 0:
                        if len(str(i * j)) == 1:
                            print(i, '*', j, '=' + ' ', i * j, end='   ')
                        else:
                            print(i, '*', j, '=', i * j, end='   ')
                        print()
                    else:
                        if len(str(i * j)) == 1:
                            print(i, '*', j, '=' + ' ', i * j, end='   ')
                        else:
                            print(i, '*', j, '=', i * j, end='   ')
                print()
            break

        else:
            for i in range(s, e+1):
                for j in range(1, 10):
                    if j % 3 == 0:
                        if len(str(i * j)) == 1:
                            print(i, '*', j, '=' + ' ', i * j, end='   ')
                        else:
                            print(i, '*', j, '=', i * j, end='   ')
                        print()
                    else:
                        if len(str(i * j)) == 1:
                            print(i, '*', j, '=' + ' ', i * j, end='   ')
                        else:
                            print(i, '*', j, '=', i * j, end='   ')
                print()
            break

'''
정답 형식

4 6
4 * 1 =  4   4 * 2 =  8   4 * 3 = 12   
4 * 4 = 16   4 * 5 = 20   4 * 6 = 24   
4 * 7 = 28   4 * 8 = 32   4 * 9 = 36   

5 * 1 =  5   5 * 2 = 10   5 * 3 = 15   
5 * 4 = 20   5 * 5 = 25   5 * 6 = 30   
5 * 7 = 35   5 * 8 = 40   5 * 9 = 45   

6 * 1 =  6   6 * 2 = 12   6 * 3 = 18   
6 * 4 = 24   6 * 5 = 30   6 * 6 = 36   
6 * 7 = 42   6 * 8 = 48   6 * 9 = 54 

------------------------------------

6 4
6 * 1 =  6   6 * 2 = 12   6 * 3 = 18   
6 * 4 = 24   6 * 5 = 30   6 * 6 = 36   
6 * 7 = 42   6 * 8 = 48   6 * 9 = 54   

5 * 1 =  5   5 * 2 = 10   5 * 3 = 15   
5 * 4 = 20   5 * 5 = 25   5 * 6 = 30   
5 * 7 = 35   5 * 8 = 40   5 * 9 = 45   

4 * 1 =  4   4 * 2 =  8   4 * 3 = 12   
4 * 4 = 16   4 * 5 = 20   4 * 6 = 24   
4 * 7 = 28   4 * 8 = 32   4 * 9 = 36   
'''