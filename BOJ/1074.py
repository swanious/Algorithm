n, r, c = map(int, input().split())
result = 0
'''
분할 정복으로 풀어나가자.
먼저, 격자판을 4분면으로 나눈다.
r, c의 위치가 어느 위치(4분면 중)에 존재하는지 좁혀나간다.
만약 3분면에 위치한다면, 
1, 2분면의 값을 다 더해주면된다.
만약 2분면에 위치한다면,
1분면의 값을 더해주고 3, 4는 날린다.

이런 과정을 되풀이하면서 좁혀나간 후 값을 구한다.
'''

# 먼저 4분면으로 나눈다.
y = pow(2, n) // 2
x = y

while n > 0:
    n -= 1
    temp = pow(2, n) // 2
    skip = pow(4, n)
    # 1분면
    if r < y and c < x:
        y -= temp
        x -= temp
    # 2분면
    elif r < y and c >= x:
        y -= temp
        x += temp
        result += skip
    # 3분면
    elif r >= y and c < x:
        y += temp
        x -= temp
        result += skip * 2  # 2개의 분면을 뛰어넘었으니
    else:
        y += temp
        x += temp
        result += skip * 3  # 2개의 분면을 뛰어넘었으니

print(result)