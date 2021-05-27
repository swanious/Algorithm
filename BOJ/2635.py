user_input = int(input())
max_li = []
max_num = 0

for i in range(user_input + 1):
    result = [user_input, i]
    j = 0
    while True:
        a = result[j] - result[j + 1]
        if a <= -1:
            break

        result.append(a)
        if max_num < len(result):
            max_num = len(result)
            max_li = result[:]
        j += 1

print(max_num)
for i in max_li:
    print(i, end=' ')