const stdin = require("fs").readFileSync("test.txt").toString().split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = null;
  }

  push = (val) => {
    const node = new Node(val);
    if (!this.head) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size++;
  }

  popleft = () => {
    if (!this.head) return null;
    const node = this.head;
    this.head = this.head.next;
    this.size--;
    return node.val;
  }

  peek = () => this.head.val;

  isEmpty = () => this.size === 0;
}

const dy = [-1, 1, 0, 0]
const dx = [0, 0, -1, 1]
const DIR = [null, [0,1,2,3], [0,1], [2,3], [0,3], [1,3], [1,2], [0,2]]
const REVERSE = {0:1, 1:0, 2:3, 3:2};

const T = +input();
for (let tc = 1; tc < T + 1; tc++) {
  // io
  let [N, M, sy, sx, t] = input().split(" ").map(Number);
  const mapp = new Array(N);
  const visit = Array.from(Array(N), () => Array(M).fill(false));
  visit[sy][sx] = true;
  for (let i = 0; i < N; i++) {
    mapp[i] = input().split(" ").map(Number);
  }

  // exec
  let ans = 1;
  const q = new Queue();
  q.push([sy, sx, mapp[sy][sx]])
  while (--t > 0) {
    let size = q.size;
    while (size-- > 0) {
      const [y, x, d] = q.popleft();
      DIR[d].forEach((dir) => {
        const ny = y + dy[dir], nx = x + dx[dir];
        if (ny >= N || nx >= M || ny < 0 || nx < 0 || visit[ny][nx] || mapp[ny][nx] === 0) return;
        if (!DIR[mapp[ny][nx]].includes(REVERSE[dir])) return;
        q.push([ny, nx, mapp[ny][nx]]);
        visit[ny][nx] = true;
        ans++;
      })
    }
  }

  console.log(`#${tc} ${ans}`);
}
