/**
shift연산
 */

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
