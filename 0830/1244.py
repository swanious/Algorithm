# 인덱스로부터 퍼져가면서 palindrom 검사(제일 큰 값 찾기)
def pal(arr, idx):
    l, r = idx - 1, idx + 1
    temp_l, temp_r = idx, idx
    while l > 0 and r < len(arr):
        if arr[l] == arr[r]:
            temp_l, temp_r = l, r
            l -= 1
            r += 1
        else:
            break
    return max(idx - temp_l, temp_r - idx)

# 출력시 20개씩 끊어주기위함
splits = 20

input()
# 배열 받기
arr = list(map(int, input().split()))
# 인덱스 계산 편의를 위해
arr.insert(0, -1)

h = int(input())

result = ''
for _ in range(h):
    sex, idx = map(int, input().split())
    if sex == 1: # 남학생
        # 자기가 받은 수의 배수의 인덱스에 존재하는 스위치 변환
        for i in range(idx, len(arr), idx):
            arr[i] = abs(arr[i] - 1)

    elif sex == 2: # 여학생
        temp_idx = pal(arr, idx)
        temp = arr[idx - temp_idx : idx + temp_idx + 1]
        for i in range(len(temp)):
            temp[i] = abs(temp[i] - 1)
        arr[idx - temp_idx: idx + temp_idx + 1] = temp

for i in range(1, len(arr), splits):
    print(*arr[i:i+splits])