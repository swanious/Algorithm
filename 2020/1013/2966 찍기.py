'''
5
BAACC
'''

n = int(input())
arr = input()

a = "ABC"
b = "BABC"
c = "CCAABB"

cnt_dict = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}

for i in range(n):
    if i % 3 == 0:
        if arr[i] == 'A':
            cnt_dict['Adrian'] += 1
    elif i % 3 == 1:
        if arr[i] == 'B':
            cnt_dict['Adrian'] += 1
    elif i % 3 == 2:
        if arr[i] == 'C':
            cnt_dict['Adrian'] += 1

    if i % 4 == 0 or i % 4 == 2:
        if arr[i] == 'B':
            cnt_dict['Bruno'] += 1
    elif i % 4 == 1:
        if arr[i] == 'A':
            cnt_dict['Bruno'] += 1
    elif i % 4 == 3:
        if arr[i] == 'C':
            cnt_dict['Bruno'] += 1

    if i % 6 == 0 or i % 6 == 1:
        if arr[i] == 'C':
            cnt_dict['Goran'] += 1
    elif i % 6 == 2 or i % 6 == 3:
        if arr[i] == 'A':
            cnt_dict['Goran'] += 1
    elif i % 6 == 4 or i % 6 == 5:
        if arr[i] == 'B':
            cnt_dict['Goran'] += 1

print(max(cnt_dict.values()))
for i in cnt_dict.items():
    if i[1] == max(cnt_dict.values()):
        print(i[0])