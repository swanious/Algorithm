// 미로탈출 - https://programmers.co.kr/learn/courses/30/lessons/81304
// 참고 - https://jun-choi-4928.medium.com/javascript%EB%A1%9C-heap-priority-queue-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-8bc13bf095d9

function solution(n, start, end, roads, traps) {
  const adj = Array.from({ length: n + 1 }, () => []);
  const rev = Array.from({ length: n + 1 }, () => []);
  const visit = Array(n + 1).fill(false);
  const isTrap = Array(n + 1).fill(false);

  roads.forEach(([from, to, dis]) => {
    adj[from].push([to, dis]);
    rev[to].push([from, dis]);
  });

  traps.forEach((trap) => (isTrap[trap] = true));

  const pq = new PQ();
  pq.push(3, [1, 2]);
  pq.push(1, [1, 2]);
  pq.push(6, [1, 2]);
  pq.push(5, [1, 2]);
  console.log(pq);
  pq.pop();
  console.log(pq);
  pq.pop();
  console.log(pq);
}

class Heap {
  constructor() {
    this.heap = [];
  }
  getLeftChildIdx = (parentIdx) => parentIdx * 2 + 1;
  getRightChildIdx = (parentIdx) => parentIdx * 2 + 2;
  getParentIdx = (childIdx) => Math.floor((childIdx - 1) / 2);

  insert = (key, value) => {
    const node = { key, value };
    this.heap.push(node);
    this.heapifyUp(); // 삽입 이후 정렬
  };
  remove = () => {
    const l = this.heap.length;
    const rootNode = this.heap[0];

    if (l === 0) return null;
    if (l === 1) return (this.heap = []);
    else {
      this.heap[0] = this.heap.pop();
      this.heapifyDown(); // 제거 이후 정렬
    }
    return rootNode;
  };

  heapifyUp = () => {
    let index = this.heap.length - 1; // 마지막 index
    const lastInsertedNode = this.heap[index]; // 마지막에 들어온 Node

    while (index > 0) {
      const parentIdx = this.getParentIdx(index);

      // 노드의 값이 더 크면 내려주기 반복
      if (this.heap[parentIdx].key > lastInsertedNode.key) {
        this.heap[index] = this.heap[parentIdx];
        index = parentIdx;
      } else break;
    }

    // 반복이후 변경된 index에 값 삽입
    this.heap[index] = lastInsertedNode;
  };
  heapifyDown = () => {
    let index = 0;
    const l = this.heap.length;
    const rootNode = this.heap[index];

    // left child 가 있을 때까지 검사
    while (this.getLeftChildIdx(index) < l) {
      const leftChildIdx = this.getLeftChildIdx(index);
      const rightChildIdx = this.getRightChildIdx(index);

      const smallerIdx =
        rightChildIdx < l &&
        this.heap[rightChildIdx].key < this.heap[leftChildIdx].key
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[smallerIdx].key <= rootNode.key) {
        this.heap[index] = this.heap[smallerIdx];
        index = smallerIdx;
      } else break;
    }

    this.heap[index] = rootNode;
  };
}

class PQ extends Heap {
  constructor() {
    super();
  }
  push = (priority, value) => this.insert(priority, value);
  pop = () => this.remove();
  isEmpty = () => this.heap.length === 0;
}
