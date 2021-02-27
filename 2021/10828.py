n = int(input())
orders = []
stack = []
cnt = 0

for i in range(n):
    orders.append(input().split())

for order in orders:
    if order[0] == 'push':
        stack.append(order[1])

    elif order[0] == 'pop':
        print(stack.pop() if stack else -1)

    elif order[0] == 'top':
        print(stack[-1] if stack else -1)

    elif order[0] == 'empty':
        print(0 if stack else 1)

    else:
        print(len(stack))
