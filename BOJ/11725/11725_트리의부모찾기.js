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

const input = [];
const strToNum = (str) => str.split(' ').map(Number);

require('readline')
  .createInterface(process.stdin, process.stdout)
  .on('line', (line) => {
    input.push(line)
  })
  .on('close', () => {
    const V = +input.shift();
    const adj = Array.from(Array(V + 1), () => []);
    const visit = new Array(V + 1).fill(false);
    input.forEach(v => {
      const [from, to] = strToNum(v);
      adj[from].push(to);
      adj[to].push(from);
    })

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
  })
