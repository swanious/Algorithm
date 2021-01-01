'''
5
55 185
58 183
88 186
60 175
46 155
'''
N = int(input())

# 사람들의 몸무게(w), 키(h)를 tuple로 받기
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))
'''
rank = 1 로 고정시켜줘서 [current의 몸무게, 키가 future보다 모두 클 경우] 바로 rank를 출력한다.
그렇지 않고, current와 future둘의 값이 서로 다르고, current값이 future값보다 작다면 rank를 올려주고 바로 출력한다.
'''
for current in people:
    # 한번 돌면 1로 초기화
    rank = 1
    for future in people:
        if current[0] != future[0] & current[1] != future[1]:
            if (current[0] < future[0]) & (current[1] < future[1]):
                rank += 1
    print(rank)