'''
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''
import sys

# 이 문제는 stack을 통해 푸는 문제가 아님
# dict를 통해서 속도를 줄여야하는 문제

n, m = map(int, input().split())
# 딕트로 받고, 결과를 담을 리스트를 만들어줌
query_dict = dict()
query_list = []
# dict의 value에 값을 저장하고
for i in range(1, n + 1):
    a = sys.stdin.readline().strip()
    query_dict[a] = i
# 찾을 값에 값이 없으면 0으로 반환, 있으면 query_list에 append하기
for i in range(n + 1, n + m):
    a = sys.stdin.readline().strip()
    if query_dict.get(a, 0):
        query_list.append(a)
# 사전 순으로 정렬
query_list.sort()
print(len(query_list))
for i in query_list:
    print(i)