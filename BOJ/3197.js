// nodejs 입출력 받는법 - https://degurii.tistory.com/108
const fs = require("fs");
const stdin =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : `10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L
`.split("\n");

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
class Q {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(val) {
    const node = new Node(val);
    if (!this.head) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size++
  }

  pop() {
    if (!this.head) return null;
    const data = this.head.val;
    this.head = this.head.next;
    this.size--;

    return data;
  }
}

// 클로져 활용 입출력 받기
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, m] = input().split(" ").map((v) => parseInt(v));
let mapp = [];
for (let i = 0; i < n; i++) {
  mapp.push(input().split(""));
}
const dy = [1, -1, 0, 0], dx = [0, 0, 1, -1];
const waterV = Array.from(Array(n), () => new Array(m).fill(false));
const swanV = Array.from(Array(n), () => new Array(m).fill(false));
let ey = 0, ex = 0, ans = 0;
let sq1 = new Q(), sq2 = new Q();
let wq1 = new Q(), wq2 = new Q();

function swan() {
  while (sq1.size > 0) {
    const [y, x] = sq1.pop();
    // swan fall in love
    if (y === ey && x === ex) return true;

    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i], nx = x + dx[i];
      if (ny < 0 || nx < 0 || ny >= n || nx >= m || swanV[ny][nx]) continue;
      if (mapp[ny][nx] === '.') {
        sq1.push([ny, nx]);
      } else {
        sq2.push([ny, nx]);
      }
      swanV[ny][nx] = true;
    }
  }
  return false;
}
function water() {
  while (wq1.size > 0) {
    const [y, x] = wq1.pop();
    mapp[y][x] = '.';

    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i], nx = x + dx[i];
      if (ny < 0 || nx < 0 || ny >= n || nx >= m || waterV[ny][nx]) continue;
      if (mapp[ny][nx] === '.') {
        wq1.push([ny, nx]);
      } else {
        wq2.push([ny, nx]);
      }
      waterV[ny][nx] = true;
    }
  }
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    // swan
    if (mapp[i][j] === 'L') {
      if (sq1.size === 0) {
        sq1.push([i, j]);
        swanV[i][j] = true;
      } else {
        ey = i, ex = j
      }
      mapp[i][j] = '.';
    }

    // water
    if (mapp[i][j] === '.') {
      wq1.push([i, j]);
      waterV[i][j] = true;
    }
  }
}
while (true) {
  water();
  if (swan()) break;
  wq1 = wq2;
  sq1 = sq2;
  wq2 = new Q();
  sq2 = new Q();
  ans++
}
