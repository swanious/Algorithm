'''
10 8
3
0 3
1 4
0 2
'''
w, h = map(int, input().split())
n = int(input())
y = [0, h]
x = [0, w]
y_new = []
x_new = []
result = 0
for i in range(n):
    temp1, temp2 = map(int, input().split())
    if temp1 == 0:
        y.append(temp2)
    else:
        x.append(temp2)
y.sort()
x.sort()
for i in range(len(y)-1):
    y_new.append(y[i+1]-y[i])
for i in range(len(x)-1):
    x_new.append(x[i+1]-x[i])

result = max(y_new) * max(x_new)
print(result)