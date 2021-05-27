import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    arr_str = ''
    max_length = 0
    for i in range(5):
        max_length = max(max_length, len(arr[i]))
    for i in range(max_length):
        for j in range(5):
            if len(arr[j]) > i:
                arr_str += arr[j][i]
            else:
                continue
    print("#{} {}".format(tc, arr_str))
