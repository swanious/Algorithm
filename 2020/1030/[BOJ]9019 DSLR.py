from collections import deque
from sys import stdin
'''
3
1234 3412
1000 1
1 16
'''
n = int(stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, stdin.readline().rstrip().split())

    result = ''
    visited = [False] * 10000


    def bfs(num, string):
        global result
        temp = 0
        temp1 = ''
        for i in range(4):
            if i == 0:
                temp = ((num * 10) % 10000) + (num * 10 // 10000)
                temp1 = 'L'
            elif i == 1:
                temp = (num % 10) * 1000 + (num // 10)
                temp1 = 'R'
            elif i == 2:
                temp = (num * 2) % 10000
                temp1 = 'D'
            elif i == 3:
                temp = 9999 if num == 0 else num - 1
                temp1 = 'S'
            if temp == b:
                result = string + temp1
                return
            if not visited[temp]:
                visited[temp] = True
                q.append((temp, string + temp1))


    q = deque()
    q.append((a, ''))
    while q:
        v = q.popleft()
        bfs(*v)
        if result != '':
            break

    print(result)
