import sys
sys.stdin = open('input.txt')

code_dict = {
    211: 0,
    221: 1,
    122: 2,
    411: 3,
    132: 4,
    231: 5,
    114: 6,
    312: 7,
    213: 8,
    112: 9,
}

h2b = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'
}

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    mapp = [list(input()) for _ in range(n)]

    binary_map = [''] * n
    ans = 0
    for i in range(n):
        for j in range(m):
            binary_map[i] += h2b[mapp[i][j]]

    for i in range(1, n):
        j = m * 4 - 1
        while j > 0:
            # 앞 행의 같은 열의 값이 현재 행의 값과 다르면(코드가 존재하면) 코드를 찾아 저장하기
            if binary_map[i][j] == '1' and binary_map[i - 1][j] == '0':
                c = [0] * 8
                for k in range(7, -1, -1):
                    x = y = z = 0
                    while binary_map[i][j] == '1': z += 1; j -= 1
                    while binary_map[i][j] == '0': y += 1; j -= 1
                    while binary_map[i][j] == '1': x += 1; j -= 1
                    while binary_map[i][j] == '0' and k: j -= 1

                    d = min(x, y, z)

                    c[k] = code_dict[x // d * 100 + y // d * 10 + z // d]
                result = (c[0] + c[2] + c[4] + c[6]) * 3 + c[1] + c[3] + c[5] + c[7]
                if result % 10 == 0: ans += sum(c)
            j -= 1
    print('#{} {}'.format(t, ans))