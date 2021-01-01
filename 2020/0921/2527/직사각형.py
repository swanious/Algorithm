'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

for i in range(4):
    a, b, c, d, A, B, C, D = map(int, input().split())

    result = ''
    # d(안만났을때)
    if c < A or D < b or d < B or C < a:
        result = 'd'

    # c(점)
    elif (c == A or C == a) and (d == B or b == D):
        result = 'c'

    # b(선분)
    elif (c == A or a == C or d == B or b == D):
        result = 'b'

    # a(겹쳤을때)
    else:
        result = 'a'

    print(result)
