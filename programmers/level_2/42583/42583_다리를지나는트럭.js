class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  enqueue = (item) => {
    const node = new Node(item);

    if (!this.head) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size++;
  };

  dequeue = () => {
    if (!this.head) return null;

    const node = this.head;
    this.head = this.head.next;
    return node.item;
  };

  peek = () => (!this.head ? 0 : this.head.item);

  isEmpty = () => this.size === 0;
}

function solution(bridge_length, weight, truck_weights) {
  const l = truck_weights.length;
  const waitingQ = new Queue();
  const q = new Queue();
  for (let i = 0; i < bridge_length; i++) {
    q.enqueue(0);
  }

  let sum_w = 0,
    count = 0;
  truck_weights.forEach((w) => {
    while (sum_w + w - q.peek() > weight) {
      sum_w -= q.dequeue();
      q.enqueue(0);
      count++;
    }
    sum_w -= q.dequeue();
    sum_w += w;
    q.enqueue(w);
    count++;
  });

  return count + bridge_length;
}
