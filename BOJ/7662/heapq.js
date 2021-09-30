class Heap {
  #getLeftChildIndex = (parentIdx) => parentIdx * 2 + 1;
  #getRightChildIndex = (parentIdx) => parentIdx * 2 + 2;
  #getParentIndex = (childIdx) => Math.floor((childIdx - 1) / 2);

  constructor() {
    this.heap = [];
    this.length = 0;
  }

  peek = () => this.heap[0];

  insert = (key, value) => {
    const node = { key, value }; // key는 우선순위, value는 값
    this.heap.push(node);
    this.heapifyUp(); // 배열에 가장 끝에 넣고, 다시 min heap의 형태를 갖추도록 한다.
    this.length++;
  };

  heapifyUp = () => {
    let index = this.heap.length - 1;
    const lastInsertedNode = this.heap[index];

    // 루트노드가 되기 전까지
    while (index > 0) {
      const parentIdx = this.#getParentIndex(index);

      if (this.heap[parentIdx].key > lastInsertedNode.key) {
        this.heap[index] = this.heap[parentIdx];
        index = parentIdx;
      } else break;
    }

    // break를 만나서 자신의 자리를 찾은 상황
    this.heap[index] = lastInsertedNode;
  };

  remove = () => {
    const l = this.heap.length;
    const rootNode = this.heap[0];

    if (l === 0) return undefined;
    if (l === 1) return (this.heap = []);
    else {
      this.heap[0] = this.heap.pop(); // 끝에 있는 노드를 부모로 만들고
      this.heapifyDown(); // 다시 min heap의 형태를 갖추도록 한다.
    }
    this.length--;
    return rootNode;
  };

  heapifyDown = () => {
    let index = 0;
    const count = this.heap.length;
    const rootNode = this.heap[index];

    // 계속해서 left child가 있을 때까지 검사한다.
    while (this.#getLeftChildIndex(index) < count) {
      const leftChildIdx = this.#getLeftChildIndex(index);
      const rightChildIdx = this.#getRightChildIndex(index);

      // 왼쪽, 오른쪽 자식 중 더 작은 노드를 찾는다.
      // 오른쪽 자식이 있으면 왼쪽 자식과 key값이 더 작은 값을 찾는다.
      const smallerChildIdx =
        rightChildIdx < count &&
        this.heap[rightChildIdx].key < this.heap[leftChildIdx].key
          ? rightChildIdx
          : leftChildIdx;

      // 자식 노드의 키 값이 루트노드보다 작으면 위로 끌어올린다.
      if (this.heap[smallerChildIdx].key <= rootNode.key) {
        this.heap[index] = this.heap[smallerChildIdx];
        index = smallerChildIdx;
      } else break;
    }

    this.heap[index] = rootNode;
  };
}

class PQ extends Heap {
  constructor() {
    super();
  }

  heappush = (priority, value) => this.insert(priority, value);
  heappop = () => this.remove();
  isEmpty = () => this.heap.length <= 0;
}

module.exports = PQ;
