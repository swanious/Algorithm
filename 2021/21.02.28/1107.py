target = input()
target_num = int(target)
n = int(input())
s = {i for i in range(10)}
result = 9999999
if n > 0:
    s = s - set(map(int, input().split()))

for i in range(1000000):
    set_i = set(map(int, list(str(i))))
    if set_i.issubset(s) and result > (len(str(i)) + abs(target_num - i)):
        result = (len(str(i))) + abs(target_num - i)
result = min(result, abs(target_num - 100))

print(result)
