#https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c
from itertools import permutations
from itertools import combinations

a = []
b = []
items= [1,2,3,4]
for i in list(combinations(items,2)):
    a.append(i)
print(a)

for i in list(permutations(items,2)):
    b.append(i)
print(b)