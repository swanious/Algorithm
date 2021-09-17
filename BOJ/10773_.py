'''
4
3
0
4
0

10
1
3
5
4
0
0
7
0
0
6
'''
n = int(input())
stack = []
for _ in range(n):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))