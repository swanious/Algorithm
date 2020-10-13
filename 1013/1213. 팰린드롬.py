from collections import deque

q = []
s = input()
result_list = []
result = deque()
flag = True
for i in s:
    q.append(i)

temp = q

i = 1
while len(temp) > 1:
    # i가 q의 길이와 같으면 break
    if i == len(q):
        flag = False
        break

    if temp[0] == temp[i]:
        a = temp.pop(i)
        b = temp.pop(0)
        result_list.append(a)
        result_list.append(b)

    else:
        i += 1

if flag == False:
    print("I'm Sorry Hansoo")
elif len(temp) == 1:
    result_list.append(*temp)


a = sorted(result_list)
while a:
    if len(a) % 2:
        temp_odd = a.pop()
        temp1 = a.pop()
        temp2 = a.pop()
        result.append(temp_odd)
        result.appendleft(temp1)
        result.append(temp2)
    else:
        temp1 = a.pop()
        temp2 = a.pop()
        result.appendleft(temp1)
        result.append(temp2)

print(''.join(result))

while True:
    # i가 q의 길이와 같으면 break
    if len(temp) <= 1 :
        flag = True
        break

    if i == len(q):
        flag = False
        break

    if temp[0] == temp[i]:
        a = temp.pop(i)
        b = temp.pop(0)
        result_list.append(a)
        result_list.append(b)

    else:
        i += 1

if flag == False:
    print("I'm Sorry Hansoo")
elif len(temp) == 1:
    result_list.append(*temp)