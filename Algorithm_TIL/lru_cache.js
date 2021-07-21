class Node {
  constructor(key, val) {
    this.key = key;
    this.val = val;
    this.prev = null;
    this.next = null;
  }
}

class LRUCache {
  constructor(limit = 5) {
    this.head = null;
    this.tail = null;
    this.size = 0;
    this.limit = limit;
    this.cache = new Map();
  }
  get(key) {
    if (!this.cache.has(key)) {
      return -1;
    } else {
      let node = this.cache.get(key);
      this.use(key);

      return node.val;
    }
  }

  set(key, val) {
    // 캐시에 값이 있을 때
    if (this.cache.get(key)) {
      const node = this.cache.get(key);

      node.val = val;

      // 위치에 따른 조건부 처리
      this.use(key);

      // cache에 값 추가
      this.cache.set(key, node);
    }

    // 캐시에 값이 없을 때
    else {
      // 캐시가 꽉 찼다면 꼬리를 자르고, 새로운 값을 넣어준다.
      if (this.size >= this.limit) {
        this.cache.delete(this.tail.key);

        this.tail = this.tail.prev;
        this.tail.next = null;
      }

      const node = new Node(key, val);
      this.size++;
      this.cache.set(key, node);

      // 캐시가 비어있었다면, head와 tail을 새로운 값으로 변경
      if (!this.head) {
        this.head = node;
        this.tail = node;
      } else {
        this.head.prev = node;
        node.next = this.head;
        this.head = node;
      }
    }
  }

  // 위치에 따라서 정렬해주는 함수
  use(key) {
    const node = this.cache.get(key);

    if (node === this.head) {
      return;
    } else if (node === this.tail) {
      node.prev.next = null;
      this.tail = node.prev;
      node.prev = null;
      node.next = this.head;
      this.head.prev = node;
      this.head = node;
    } else {
      if (node.prev) {
        node.prev.next = node.next;
      }
      if (node.next) {
        node.next.prev = node.prev;
      }

      node.next = this.head;
      node.prev = null;
      this.head.prev = node;
      this.head = node;
    }
  }
}
