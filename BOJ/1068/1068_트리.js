const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

let N;
let nodes;
let target;
rl.on("line", (line) => {
  if (!N) N = +line;
  else if (!nodes) nodes = line.split(" ").map(Number);
  else if (!target) target = +line;
});
rl.on("close", () => {
  const visit = new Array(N).fill(false);
  const arr = Array.from(Array(N), () => []);

  let ans = 0;
  for (let i = 1; i < N; i++) {
    arr[nodes[i]].push(i);
  }

  // dfs
  function dfs(node) {
    visit[node] = true;
    if (node === target) return;

    for (let w of arr[node]) {
      if (visit[w] || w == target) continue;
      if (!arr[w].length) ans++;
      visit[w] = true;
      dfs(w);
    }
  }
  dfs(0);
  console.log(ans);

  process.exit();
});
