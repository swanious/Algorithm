code_dict = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        temp = input()
        code_list = []
        while temp:
            if code_dict.get(temp[:7]):
                code_list.append(int(code_dict[temp[:7]]))
                temp = temp[7:]
            else:
                temp = temp[7:]

        result = 0
        if len(code_list) != 8:
            continue
        else:
            for i in range(len(code_list) - 1):
                if i % 2 == 0:
                    result += code_list[i] * 3

                else:
                    result += code_list[i]
            result += code_list[len(code_list) - 1]

        if result == m:
            ans = sum(code_list)
        else:
            continue

    print('#{} {}'.format(t, ans))
