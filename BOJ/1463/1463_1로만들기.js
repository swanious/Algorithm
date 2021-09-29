const stdin = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const number = +input();

const q = [];
const visit = new Array(Math.pow(10, 6)).fill(false);
visit[number] = true;

q.push([number, 0]);
while (q.length > 0) {
  let [num, cnt] = q.shift();
  if (num === 1) {
    console.log(cnt);
    break;
  }

  const d3 = num / 3;
  const d2 = num / 2;

  if (Number.isInteger(num / 3) && !visit[d3]) {
    visit[d3] = true;
    q.push([d3, cnt + 1]);
  }
  if (Number.isInteger(num / 2) && !visit[d2]) {
    visit[d2] = true;
    q.push([d2, cnt + 1]);
  }
  if (!visit[num - 1]) {
    visit[num - 1] = true;
    q.push([num - 1, cnt + 1]);
  }
}
