const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n, m] = input[0].split(" ");
n = parseInt(n);
m = parseInt(m);

let flag = false;
let G = new Array(n + 1);
let map = new Array(n + 1);
let visit = new Array(n + 1);
let answer = 0;

for (let i = 0; i < n + 1; i++) {
  G[i] = new Array(n + 1);
  G[i].fill(0);
}

for (let i = 0; i < map.length; i++) {
  map[i] = [];
}

for (let i = 1; i < n; i++) {
  let temp = input[i].split(" ");
  temp = temp.map((a) => parseInt(a));
  G[temp[0]][temp[1]] = temp[2];
  G[temp[1]][temp[0]] = temp[2];
  map[temp[0]].push(temp[1]);
  map[temp[1]].push(temp[0]);
}

for (let i = n; i < input.length; i++) {
  visit = new Array(n + 1);
  answer = 0;
  flag = false;
  let temp = input[i].split(" ");
  let a = parseInt(temp[0]);
  let b = parseInt(temp[1]);

  if (map[a].includes(b)) {
    console.log(G[a][b]);
    continue;
  } else {
    visit[a] = true;
    dfs(a, b);
  }
}

function dfs(v, target) {
  if (map[v].includes(target)) {
    flag = true;
    answer += G[v][target];
    console.log(answer);
    return;
  }

  for (const w of map[v]) {
    if (flag) return;
    if (visit[w]) continue;
    else {
      visit[w] = true;
      answer += G[v][w];
      dfs(w, target);
      visit[w] = false;
      answer -= G[v][w];
    }
  }
}
