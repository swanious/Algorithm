const stdin = require("fs").readFileSync("test.txt").toString().split("\r\n");
const input = (() => {
  let l = 0;
  return () => stdin[l++];
})();

const zip = (arr) => {
  const result = [];
  for (let i = 0; i < N; i++) {
    let temp = [];
    for (let j = 0; j < N; j++) {
      temp.push(arr[j][i]);
    }
    result.push(temp);
  }

  return result;
};

// io
const N = +input();
const arr = [];
for (let i = 0; i < N; i++) {
  arr.push(input().split(" ").map(Number));
}

// exec
const newArr = zip(arr);
newArr.sort((a, b) => b[N - 1] - a[N - 1]);

let idxs = new Array(N).fill(N - 1);
let i = 0;
let ans = 0;
let cnt = N;
while (cnt-- > 0) {
  let max = 0;
  let idx = 0;
  for (let j = 0; j < N; j++) {
    if (i === j) continue;
    if (newArr[j][idxs[j]] >= max) {
      max = newArr[j][idxs[j]];
      idx = j;
    }
  }
  if (!cnt) {
    ans = idx;
    break;
  }
  idxs[idx]--;
  i = ++i % N;
}

console.log(newArr[ans][idxs[ans]]);
