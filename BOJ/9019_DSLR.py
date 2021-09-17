from collections import deque


def bfs(number, string):
    global result

    temp = 0
    temp1 = ''
    for i in range(4):
        if i == 0:
            temp = ((number * 10) % 10000) + (number * 10 // 10000)
            temp1 = 'L'
        elif i == 1:
            temp = (number // 10) + ((number % 10) * 1000)
            temp1 = 'R'
        elif i == 2:
            if number == 0:
                temp = 9999
                temp1 = 'S'
            else:
                temp = number - 1
                temp1 = 'S'
        elif i == 3:
            temp = (number * 2) % 10000
            temp1 = 'D'

        if temp == B:
            result = string + temp1
            return

        if not visit[temp]:
            visit[temp] = True
            queue.append((temp, string + temp1))


for _ in range(int(input())):
    A, B = map(int, input().split())

    visit = [False] * 10000
    result = ''

    queue = deque()
    queue.append((A, ''))
    while queue:
        v = queue.popleft()
        bfs(v[0], v[1])
        if result != '':
            break

    print(result)
