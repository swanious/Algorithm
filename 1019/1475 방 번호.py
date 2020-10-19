n = input()
num_cnt = [0] * 10
number_list = []
cnt = 0
for i in list(str(n)):
    number_list.append(int(i))
for i in number_list:
    num_cnt[i] += 1
for i in range(len(num_cnt)):
    if num_cnt[6]:
        num_cnt[9] += num_cnt[6]
        num_cnt[6] = 0

if num_cnt[-1] % 2:
    num_cnt[9] = num_cnt[9] // 2 + 1
else:
    num_cnt[9] = num_cnt[9] // 2
print(max(num_cnt))