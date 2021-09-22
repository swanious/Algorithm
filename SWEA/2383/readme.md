# 2383 점심식사시간

> [문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl)

## 설계

1. 사람의 수는 최대 10명, 계단은 2개로 고정이므로 각 계단으로 이동할 수 있는 모든 경우의 수를 구해준다(조합)
   - 조합을 구하기 전 각 사람의 좌표(y, x)를 계단과의 거리(d1, d2)로 초기화해주니까 훨씬 수월했다.
   - 조합을 구하기 위해 check배열을 초기화하여 dfs 재귀를 통한 조합을 구할 수 있도록한다.
2. `dfs(idx)`에서 조합을 구한 후, 구해진 조합을 통해 `calc(이동 중인 사람배열, 계단의 높이)` 함수로 시간을 계산한다.
3. `calc()`함수에서 시간을 구하기 위해 크게 3부분으로 나눠서 생각한다.

   - `계단으로 이동중인 사람이 있거나`, `대기중인 사람이 있거나`, `계단을 내려가는 사람이 있으면` 반복한다.
     1. 대기중인 사람이 있을때 내려가는 사람들의 배열이 3명 미만일때 `processing`에 추가하고 waiting - 1
     2. `processing`배열을 돌면서 사람들의 시간을 -1씩 해준다. 이후, 다 내려간 사람(거리가 0인 사람)은 processing에서 제거한다.
     3. 계단으로 이동중인 사람배열인 `s_people`배열을 돌면서 시간을 -1씩 해준다. 계단에 사람이 도착하면(값이 0) waiting + 1해준다.

4. `calc()`함수에서 구한 계단1, 계단2의 시간 중 큰 값(계단1에서 다 내려갔다해도 계단2에 사람이 남았으면 그 시간이 최종 시간이므로)과 기존의 값 중 작은 값이 정답

## 나의 코드

```python
import sys
sys.stdin = open('test.txt','r')

def get_dis(ey, ex, y, x):
    return abs(ey - y) + abs(ex - x)

# 이동중인사람들, 계단높이
def calc(s_people, height):
    count, waiting = 0, 0
    processing = [] # 내려가는 사람
    while s_people or waiting or processing:

        # 계단을 내려가는 사람의 수가 3명이면 break 아니면 추가
        while waiting:
            if len(processing) == 3:
                break
            processing.append(height)
            waiting -= 1

        # 내려가는 사람들의 시간을 -1씩
        for i in range(len(processing)-1, -1, -1):
            processing[i] -= 1
            if processing[i] == 0:
                processing.pop(i)

        # 계단으로 이동중인 사람들의 시간을 -1씩
        for i in range(len(s_people)-1, -1, -1):
            s_people[i] -= 1
            if s_people[i] == 0:
                s_people.pop(i)
                waiting += 1

        count += 1
    return count

def dfs(idx):
    global min_count

    if idx == nums:
        s1_people, s2_people = [], []
        for i in range(nums):
            if check[i]: s1_people.append(p_li[i][0])
            else: s2_people.append(p_li[i][1])


        count = max(calc(sorted(s1_people), s_li[0][2]), calc(sorted(s2_people), s_li[1][2]))
        min_count = min(count, min_count)
        return

    check[idx] = True
    dfs(idx + 1)
    check[idx] = False
    dfs(idx + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    nums, min_count = 0, 987654321
    p_li, s_li = [], []

    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 1:
                p_li.append([i, j])
                nums += 1
            elif mapp[i][j] > 1:
                s_li.append([i, j, mapp[i][j]])
    check = [False] * nums

    # [y, x] -> [계단1과의 거리, 계단2와의 거리] 초기화
    for i in range(nums):
        d1 = get_dis(s_li[0][0], s_li[0][1], p_li[i][0], p_li[i][1])
        d2 = get_dis(s_li[1][0], s_li[1][1], p_li[i][0], p_li[i][1])
        p_li[i][0] = d1
        p_li[i][1] = d2


    dfs(0) # 조합 구하기
    print("#{} {}".format(tc, min_count + 1)) # 1분 추가
```

```javascript
// 입출력
const stdin = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const input = (() => {
  let l = 0;
  return () => stdin[l++];
})();

const N = Number(input());
const lines = [];
let ans = 0,
  check = false,
  start = 0,
  end = 0;

// 로직
for (let i = 0; i < N; i++) {
  lines.push(input().split(" ").map(Number));
}

lines.sort((a, b) => a[0] - b[0]);

for (let line of lines) {
  if (!check) {
    start = line[0];
    end = line[1];
    check = true;
    continue;
  }

  if (line[0] <= end) {
    end = Math.max(line[1], end);
  } else {
    ans += end - start;
    start = line[0];
    end = line[1];
  }
}
ans += end - start;
console.log(ans);
```

## 후기

- swea 시뮬레이션은 시간이 너무 오래걸린다..ㅠ 그래도 실력은 느는느낌이라 안도감 + 1
