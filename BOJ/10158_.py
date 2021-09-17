'''
6 4
4 1
8
'''

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

t_x = 0
if ((x + t) // w) % 2 == 0:
    t_x = (x + t) % w
else:
    t_x = w - ((x + t) % w)

t_y = 0
if ((y + t) // h) % 2 == 0:
    t_y = (y + t) % h
else:
    t_y = h - ((y + t) % h)
print(t_x, t_y)