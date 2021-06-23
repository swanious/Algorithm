class Stack {
  constructor() {
    this.top = -1;
    this.stackArray = [];
  }
  push(element) {
    this.top++;
    this.stackArray[this.top] = element;
  }
  pop() {
    if (this.top > -1) {
      let temp = this.stackArray[this.top];
      this.top--;
      return temp;
    }
    return null;
  }
  isEmpty() {
    return this.top === -1;
  }
  peek() {
    return this.stackArray[this.top];
  }
  get length() {
    return this.top + 1;
  }
  clear() {
    this.top = -1;
    this.stackArray = [];
  }
}

class Queue {
  constructor() {
    this.inBox = new Stack();
    this.outBox = new Stack();
  }
  enqueue(element) {
    this.inBox.push(element);
  }
  dequeue() {
    if (this.outBox.isEmpty()) {
      while (!this.inBox.isEmpty()) {
        this.outBox.push(this.inBox.pop());
      }
    }
    return this.outBox.pop();
  }
  size() {
    return this.inBox.length + this.outBox.length;
  }
}
const q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
console.log(q.dequeue());
console.log(q.dequeue());
console.log(q.dequeue());
