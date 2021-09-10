const fs = require('fs');
const stdin = (fs.readFileSync('/dev/stdin').toString()).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const arr = [];
const [n, m] = input().split(' ').map(Number);
const visit = new Array(n+1).fill(false);
const dfs = function(v) {
  if (arr.length === m) {
    console.log(...arr)
    return 
  }

  for (let i = 1; i < n+1; i++) {
    if (!visit[i]) {
      visit[i] = true;
      arr.push(i)
      dfs(i + 1)
      arr.pop()
      visit[i] = false;
    }
  }
}

dfs(n)
