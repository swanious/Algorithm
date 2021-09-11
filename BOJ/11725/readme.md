# 11725 트리의부모찾기
> [문제 링크](https://www.acmicpc.net/problem/11725)

## JS 코드
```javascript
const fs = require('fs')
const stdin = (fs.readFileSync('tc.txt').toString()).split('\n')
// const stdin = (fs.readFileSync('/dev/stdin').toString()).split('\n')

const input = (() => {
  let line = 0;
  return () => stdin[line++]
})()
class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}
class Q {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  append (item) {
    const node = new Node(item);
    if (!this.head) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size++
  }
  
  popleft () {
    if (!this.head) return null;
    const item = this.head.item;

    this.head = this.head.next;
    this.size--;

    return item
  }

  isEmpty () {
    return this.size === 0;
  }
}

const V = +input();
const adj = Array.from(Array(V + 1), () => []);
const visit = new Array(V + 1).fill(false);
for (let i = 0; i < V-1; i++) {
  const [from, to] = input().split(' ').map(Number);
  adj[from].push(to);
  adj[to].push(from);
}

const q = new Q();
let answer = new Array(V + 1);
answer[1] = 0;
q.append(1);
visit[1] = true;
while (!q.isEmpty()) {
  const v = q.popleft();
  for (let w of adj[v]) {
    if (!visit[w]) {
      visit[w] = true;
      q.append(w);
      answer[w] = v;
    }
  }
}
answer.forEach((v, i) => { if (i > 1) console.log(v) })
```

## 후기
- 똑같은 로직으로 python에서 풀면 빠른 시간으로 통과하는데,
- js기본 배열의 shift연산으로 처리하니까 시간초과, 그래서 링크드리스트로 Q를 만들었지만 또 시간초과..
- 아무래도 입출력 부분이 문제인거같다. 백준에서 js로 문제풀기 까다롭다 ㅠ