'''
9
SLLLLSSLL
'''

n = int(input())
s = input()

L_cnt = s.count('LL')

if L_cnt <= 1: print(n)
else: print(n - L_cnt + 1)