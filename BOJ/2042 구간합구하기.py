'''
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
'''
import sys


def guganhap(start, end, depth, idx, front, back, mapp):
    # print(start, end, depth, idx, front, back, mapp[depth][idx])
    mid = (front + back) >> 1
    if start == end:  # 구하고자 하는 구간의 길이가 1이다 : 그 인덱스 자체의 위치에 있는 값을 바로 가져옴
        return mapp[0][start]

    if depth == 0:
        return mapp[0][idx]  # 구간 끝까지 올라가면, 찾는값을 준다

    if start == front and end == back:  # 원하는 구간이면 바로 가져온다.
        return mapp[depth][idx]

    elif end <= mid:  # 오른쪽을 볼 필요없을 경우에는
        return guganhap(start, end, depth - 1, idx * 2, front, mid, mapp)  # 왼쪽 길만 돌아본다.

    elif mid < start:  # 왼쪽값을 볼 필요없을 경우에는
        return guganhap(start, end, depth - 1, idx * 2 + 1, mid + 1, back, mapp)  # 오른쪽 길만 돌아본다.

    else:  # 구간이 왼쪽, 오른쪽 둘다 봐야할 경우
        return guganhap(start, mid, depth - 1, idx * 2, front, mid, mapp) + guganhap(mid + 1, end, depth - 1, idx*2 + 1, mid + 1, back, mapp)


n, m, k = map(int, sys.stdin.readline().rstrip().split())

# 첫 숫자배열 받기
number_list = []
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    number_list.append(temp)

# 트리 구조 만들어주기 (i, i+1 값을 더해주면서 내려가는 구조)
mapp = [number_list]
while len(number_list) > 1:
    new_list = []
    sum = 0
    for i in range(0, len(number_list), 2):
        if i + 1 == len(number_list):
            new_list.append(number_list[i])
            continue
        sum = number_list[i] + number_list[i + 1]
        new_list.append(sum)
    mapp.append(new_list)
    number_list = new_list

result = 0

# 미션 1, 2 수행 부분
for i in range(m + k):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    # 수를 바꾼다(트리구조 또한 바꾼다)
    if temp[0] == 1:
        idx = temp[1] - 1  # 가져온 인덱스 수정
        mapp[0][idx] = temp[2]  # 가져온 인덱스의 값을 변경
        for j in range(1, len(mapp)):
            if (len(mapp[j - 1]) % 2 == 1) and (idx + 1) == len(mapp[j - 1]):
                idx = idx // 2
                mapp[j][idx] = mapp[j - 1][idx * 2]
                continue
            idx = idx // 2
            sum = mapp[j - 1][idx * 2] + mapp[j - 1][idx * 2 + 1]
            mapp[j][idx] = sum

    # 구간합을 구한다.
    else:
        idx1 = temp[1] - 1  # start idx
        idx2 = temp[2] - 1  # end idx
        result = guganhap(idx1, idx2, len(mapp) - 1, 0, 0, (1 << (len(mapp) - 1)) - 1, mapp)  # 구간 합
        print(result)
