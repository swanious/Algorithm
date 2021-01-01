l, n = map(int, input().split())
s = list(input().split())
s.sort()

aioue = ['a', 'i', 'o', 'u', 'e']
result = [''] * l


def find(idx, a, arr):
    if a == len(arr):
        moum = 0
        jaum = 0
        for i in range(l):
            if arr[i] in aioue:
                moum += 1
            else:
                jaum += 1

        if jaum < 2 or moum < 1:
            return

        else:
            print(''.join(arr))
            return

    if idx == n:
        return

    arr[a] = s[idx]
    find(idx + 1, a + 1, arr)
    find(idx + 1, a, arr)

find(0, 0, result)


'''
from itertools import combinations
l, c = map(int,input().split())
alpha = sorted(list(input().split()))

candidate = list(combinations(alpha,l))

for candi in candidate:
    num_v = 0
    num_c = 0
    for c in candi:
        if c in "aeiou":
            num_v +=1
        else:
            num_c +=1
    
    if num_v >=1 and num_c>=2:
        print(''.join(candi))
'''