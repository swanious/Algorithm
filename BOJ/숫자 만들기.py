import sys;
from collections import deque
from copy import deepcopy

sys.stdin = open('input.txt')


def perm(k, n):
    if k == n:
        if not ''.join(operator) in oper_list:
            oper_list.append(''.join(operator))
            return

    else:
        for i in range(k+1, n):
            if operator[k] == operator[i]:
                perm(k + 1, n)
            else:
                operator[k], operator[i] = operator[i], operator[k]
                perm(k + 1, n)
                operator[k], operator[i] = operator[i], operator[k]


for tc in range(1, int(input()) + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    num = list(map(int, input().split()))
    temp1 = ['+', '-', '*', '/']

    # 연산자 list로 변환
    idx = 0
    temp2 = ''
    operator = ''
    while idx < 4:
        operator += temp1[idx] * temp[idx]
        idx += 1

    operator = list(operator)

    # 피연산자를 담아둘 리스트(str)
    oper_list = []
    perm(0, len(operator))

    q = deque()
    for i in num:
        q.append(i)
    temp_q = deepcopy(q)
    # 계산
    ans = []
    for i in range(len(oper_list)):
        j = 0
        q = deepcopy(temp_q)
        while j < len(oper_list[0]):
            if len(q) == 1:
                ans.append(q[0])
                break
            else:
                a = q.popleft()
                b = q.popleft()
                if oper_list[i][j] == '+':
                    q.appendleft(a + b)
                    j += 1
                elif oper_list[i][j] == '-':
                    q.appendleft(a - b)
                    j += 1
                elif oper_list[i][j] == '*':
                    q.appendleft(a * b)
                    j += 1
                elif oper_list[i][j] == '/':
                    q.appendleft(int(a / b))
                    j += 1
        ans.append(q[0])
    print('#{} {}'.format(tc, max(ans) - min(ans)))
