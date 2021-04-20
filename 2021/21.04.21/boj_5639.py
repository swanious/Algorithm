import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if nodes[start] < nodes[i]:
            division = i
            break

    post_order(start + 1, division - 1)
    post_order(division, end)
    print(nodes[start])


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

post_order(0, len(nodes) - 1)
