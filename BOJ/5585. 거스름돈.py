n = int(input())

mc = 1000 - n
result = 0

result = mc // 500
mc %= 500
result += mc // 100
mc %= 100
result += mc // 50
mc %= 50
result += mc // 10
mc %= 10
result += mc // 5
mc %= 5
result += mc // 1

print(result)