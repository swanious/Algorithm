# 2170 선긋기
> [문제 링크](https://www.acmicpc.net/problem/2170)

## 설계
1. 시작점부터 오름차순 정렬
2. 첫 라인은 start, end를 초기화 후 continue
3. (if) 이후의 line의 시작점이 end보다 작으면(선이 겹침) end를 큰 값으로 초기화
4. (else) 선이 안겹치면 start, end 새로 초기화
5. 반복문이 끝나면 ans에 마지막 선의 길이 더해주고 출력

## 나의 코드
```python
import sys

input = sys.stdin.readline
lines = []

for i in range(int(input())):
    lines.append(list(map(int, input().split())))

lines.sort(key = lambda x: x[0])

check = False
start, end = 0, 0
ans = 0

for line in lines:
    if not check:
        start = line[0]
        end = line[1]
        check = True
        continue

    if line[0] <= end:
        end = max(end, line[1])

    else:
        ans += end - start
        start = line[0]
        end = line[1]
        
ans += end - start
print(ans)
```

```javascript
// 입출력
const stdin = (require('fs').readFileSync('/dev/stdin').toString()).split('\n')
const input = (() => {
  let l = 0;
  return () => stdin[l++]
})()


const N = Number(input())
const lines = [];
let ans = 0, check = false, start = 0, end = 0;

// 로직
for (let i=0; i<N; i++) {
  lines.push(input().split(' ').map(Number))
}

lines.sort((a, b) => a[0] - b[0])

for (let line of lines) {
  if (!check) {
    start = line[0];
    end = line[1];
    check = true;
    continue
  }
  
  if (line[0] <= end) {
    end = Math.max(line[1], end)
  }
  
  else {
    ans += end - start;
    start = line[0];
    end = line[1];
  }
}
ans += end - start
console.log(ans)
```

## 후기
- 정렬문제 !