target_channel = int(input())
n = int(input())
broken_buttons = list(map(int, input().split()))

number_list = list(range(10))
for button in broken_buttons:
    number_list.remove(button)

big = ''
small = ''
pre_big = ['up']
pre_small = []

for i in target_channel:
    if i in number_list:
        big += str(i)
        small += str(i)
        pre_big = [str(i)]
        pre_small = [str(i)]
        for j in range(i + 1, 10):
            if j in number_list:
                pre_big.append(str(j))
                break
        if len(pre_big) == 1:
            pre_big.append('up')

        for j in range(i, -1, -1):
            if j in number_list:
                pre_small.append(str(j))
                break
        if len(pre_small) == 1:
            pre_small.append('down')

    else:
        for j in range(i, 10):
            if j in number_list:
                big += str(j)
                big += str(min(number_list))*(len(number_list)-count-1)
