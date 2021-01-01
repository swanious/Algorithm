# yield(담아두기), next(다음 값 출력)
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()
for _ in range(100):
    print(next(g))

# range 클래스 이해
a = [n for n in range(100000)] # 실제 값이 a안에 존재
b = range(100000) # 생성 조건만 b안에 존재

# enumerate
a = [1, 2, 3, 2, 45, 2, 5]

for i, v in enumerate(a):
    print(i, v)
print(list(enumerate(a)))  # [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]
