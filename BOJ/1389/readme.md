# 2170 선긋기

> [문제 링크](https://www.acmicpc.net/problem/2170)

## 설계

- 인접리스트로 bfs 완전탐색하면 해결할 수 있음
- 자신의 depth를 가지고 다니면서 더해주고 ans배열에서 가장 값이 작은 index 뽑아주면 됨(js의 indexOf와 Math.min을 사용하면 조건에 부합하는 첫 인덱스를 가져올 수 있음)

## 나의 코드

```javascript
const stdin = require("fs").readFileSync("test.txt").toString().split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// io
const [N, M] = input().split(" ").map(Number);
const ans = new Array(N + 1).fill(0);
const adj = Array.from(Array(N + 1), () => []);
for (let i = 0; i < M; i++) {
  const [a, b] = input().split(" ").map(Number);
  adj[a].push(b);
  adj[b].push(a);
}

// exec
for (let i = 1; i < N + 1; i++) {
  const q = [];
  const visit = new Array(N + 1).fill(false);
  q.push([i, 0]);
  visit[i] = true;

  while (q.length > 0) {
    const [v, cnt] = q.shift();
    ans[i] += cnt;
    for (let w of adj[v]) {
      if (visit[w]) continue;
      visit[w] = true;
      q.push([w, cnt + 1]);
    }
  }
}
console.log(ans.indexOf(Math.min(...ans.slice(1))));
```

```javascript

```

## 후기

- 기본적인 bfs 문제
