from collections import deque


s = input()
cnt_list = [0] * 26
odd_str = ''
# cnt_list에 각 알파벳 순서에 맞게 cnt를 올려줌
for i in s:
    cnt_list[ord(i) - 65] += 1

temp_cnt = cnt_list[:]
pal_str = ''
# temp 각 알파벳 수에 2를 나눈 나머지를 채워줌(합이 1초과면 팰린드롬이 아님)
for i in range(26):
    temp_cnt[i] = temp_cnt[i] % 2

for i in range(26):
    # temp_cnt의 합이 1 초과면 팰린드롬 X
    if sum(temp_cnt) > 1:
        print("I'm Sorry Hansoo")
        break
    # temp_cnt를 두 가지로 나눠볼 수 있음.
    # 모두 0일 경우(짝수), 존재할 경우(홀수)
    else:
        if temp_cnt[i] == 1:
            odd_str += chr(i + 65)
            temp_cnt[i] -= 1
            pal_str += chr(i + 65) * cnt_list[i]
        else:
            pal_str += chr(i + 65) * cnt_list[i]

# 결과 -> 왼쪽, 오른쪽 append를 위해 deque로 받아줌
# 홀수일 경우, pal_str에서 odd_str을 빼줌(따로 받기 위해)
result = deque()
pal_str = pal_str.replace(odd_str, '', 1)
temp = list(pal_str)

if len(temp) == 0 and odd_str:
    print(odd_str)
else:
    while temp:
        if odd_str:
            result.append(odd_str)
            odd_str = ''
            a = temp.pop()
            b = temp.pop()
            result.appendleft(a)
            result.append(b)
        else:
            a = temp.pop()
            b = temp.pop()
            result.appendleft(a)
            result.append(b)
print(''.join(result))