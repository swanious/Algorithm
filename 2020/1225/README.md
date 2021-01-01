# jungol_1335 색종이 만들기

예전에 풀었던 기억이 있지만 다시 풀어보니 분할정복에 대해 제대로 이해하지 못했다는 것을 깨달았다.. 그 이유는, 문제를 보고 해답을 떠올리는데 오랜시간을 쓰기도 했고 결국 블로그 찬스를 썼다ㅠ

이후 혼자 힘으로 2번을 다시 풀어봤다 ! 그러니까 어느정도는 이해할 수 있었다.



- 분할하기 전 
  - 색의 갯수(tmp)가 n ** 2(배열의 크기)와 같으면,  파란색으로 찼다는 의미이므로 `b_cnt`를 +1
  - 색의 갯수(tmp)가 0 이면,  하얀색으로 찼다는 의미이므로 `w_cnt`를 +1
- 분할
  - 색이 다를 경우 분할을 시작한다.(재귀)
  - 더 이상 분할할 수 없다면, 색의 갯수를 세어주고 return한다. 이후 다음 재귀를 실행

```python
def div_conq(y, x, n):
    global b_cnt, w_cnt

    tmp = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if B[i][j]:
                tmp += 1

    if tmp == n ** 2:
        b_cnt += 1
    elif not tmp:
        w_cnt += 1
    else:
        # 분할정복
        div_conq(y, x, n // 2)  # y, x의 인덱스가 0~3일 때
        div_conq(y, x + n // 2, n // 2)  # y가 0~3, x가 4~7일 때
        div_conq(y + n // 2, x, n // 2)  # y가 4~7, x가 0~3일 때
        div_conq(y + n // 2, x + n // 2, n // 2)  # y가 4~7, x가 4~7일 때

    return


n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
b_cnt, w_cnt = 0, 0

div_conq(0, 0, n)
print(w_cnt, b_cnt)

```

