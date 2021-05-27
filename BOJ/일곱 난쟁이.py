'''
20
7
23
19
10
15
25
8
13
'''
stack = []
for i in range(9):
    stack.append(int(input()))

res = sum(stack)
stack.sort()
for i in range(9):
    for j in range(i+1, 9):
        if res - stack[i] - stack[j] == 100:
            for k in range(9):
                if k == i or k == j: continue
                else:
                    print(stack[k])
