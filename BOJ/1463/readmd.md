# 1463 1로 만들기

> [문제 링크](https://www.acmicpc.net/problem/1463)

## 설계

- 최소값을 구하는 문제이므로 bfs로 풀이했다.
- 유의할 점은 똑같은 값이 중복해서 들어가지 않도록 해야한다.
- 10^6 크기의 visit배열을 생성해서 `3으로 나눈 값`, `2로 나눈 값`, `1을 뺀 값`을 안갔을 경우에만 q에 집어넣는다.

## 나의 코드

```javascript
const stdin = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const number = +input();

const q = [];
const visit = new Array(Math.pow(10, 6)).fill(false);
visit[number] = true;

q.push([number, 0]);
while (q.length > 0) {
  let [num, cnt] = q.shift();
  if (num === 1) {
    console.log(cnt);
    break;
  }

  const d3 = num / 3;
  const d2 = num / 2;

  if (Number.isInteger(num / 3) && !visit[d3]) {
    visit[d3] = true;
    q.push([d3, cnt + 1]);
  }
  if (Number.isInteger(num / 2) && !visit[d2]) {
    visit[d2] = true;
    q.push([d2, cnt + 1]);
  }
  if (!visit[num - 1]) {
    visit[num - 1] = true;
    q.push([num - 1, cnt + 1]);
  }
}
```

## 후기

- visit처리를 통해 중복을 제거하면 bfs로 쉽게 풀 수 있다.
