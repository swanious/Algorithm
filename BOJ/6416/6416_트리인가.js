const fs = require("fs");
const stdin = fs.readFileSync("test.txt").toString().split("\n");
const input = (function () {
  let l = 0;
  return () => stdin[l++];
})();

const strToNum = (str) => str.split(" ").map(Number);

const checkHaveOneRootNode = (obj) => {
  let rootNode = Object.entries(parents).filter(([k, v]) => !v);
  let count = rootNode.length === 1;
  return [rootNode[0][0], count];
};

const solution = (rootNode, adj) => {
  let visit = [];
  adj.forEach((nodes) => nodes.forEach((v) => (visit[v] = false)));
  visit[rootNode] = true;
  const dfs = (v) => {
    if (!adj[v]) return;
    for (let w of adj[v]) {
      if (!visit[w]) {
        visit[w] = true;
        dfs(w);
      }
    }
  };
  dfs(rootNode);
  return visit.filter((v) => v).length;
};

const ioExec = (inputString) =>
  inputString == ["-1 -1"]
    ? false
    : inputString
        .split("  ")
        .filter((v) => v)
        .map((v) => strToNum(v));

let tc = 1;
let adj = [];
let parents = {};
let validation = true; // 2. 부모가 두명인 경우 체크

while (true) {
  let last = false;
  const tmp = ioExec(input());
  if (!tmp) break; // 마지막 처리
  if (!tmp.length) continue; // 공백 스킵

  tmp.forEach(([from, to]) => {
    if (!from) {
      last = true;
      return;
    }
    adj[from] ? adj[from].push(to) : (adj[from] = [to]);
    parents[from] = undefined; // 루트노드 찾기위해 초기화
    parents[to] ? (validation = false) : (parents[to] = from);
  });

  if (last) {
    const [rootNode, hasOneRoot] = checkHaveOneRootNode(parents);
    const visitCount = solution(rootNode, adj);
    const nodeCount = Object.keys(parents).length;
    if (!validation || !hasOneRoot || visitCount !== nodeCount) {
      console.log(`Case ${tc} is not a tree.`);
    } else {
      console.log(`Case ${tc} is a tree.`);
    }
    tc++;
    adj = [];
    parents = {};
    validation = true;
    continue;
  }
}
