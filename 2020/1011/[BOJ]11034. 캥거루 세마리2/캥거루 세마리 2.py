import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())

    if b - a < c - b:
        print(c - b - 1)
    else:
        print(b - a - 1)