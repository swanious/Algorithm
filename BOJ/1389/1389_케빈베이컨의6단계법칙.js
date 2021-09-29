const stdin = require("fs").readFileSync("test.txt").toString().split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// io
const [N, M] = input().split(" ").map(Number);
const ans = new Array(N + 1).fill(0);
const adj = Array.from(Array(N + 1), () => []);
for (let i = 0; i < M; i++) {
  const [a, b] = input().split(" ").map(Number);
  adj[a].push(b);
  adj[b].push(a);
}

// exec
for (let i = 1; i < N + 1; i++) {
  const q = [];
  const visit = new Array(N + 1).fill(false);
  q.push([i, 0]);
  visit[i] = true;

  while (q.length > 0) {
    const [v, cnt] = q.shift();
    ans[i] += cnt;
    for (let w of adj[v]) {
      if (visit[w]) continue;
      visit[w] = true;
      q.push([w, cnt + 1]);
    }
  }
}
console.log(ans.indexOf(Math.min(...ans.slice(1))));
