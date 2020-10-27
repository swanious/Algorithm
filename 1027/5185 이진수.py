'''
3
4 47FE
5 79E12
8 41DA16CD
'''

num_dict = {
    '0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}
T = int(input())
for tc in range(1, T + 1):
    temp = input().split()
    num_str = temp[-1]
    num_list = []

    # 숫자 변환
    for i in num_str:
        num_list.append(num_dict[i])

    def binary(num):
        result = ''
        num = int(num)
        while num:
            result += str(num % 2)
            num //= 2
        if len(result) != 4:
            while len(result) != 4:
                result += '0'
        result = result[::-1]
        return result

    result = ''
    for i in num_list:
        a = binary(i)
        result += a
    print('#{} {}'.format(tc, result))