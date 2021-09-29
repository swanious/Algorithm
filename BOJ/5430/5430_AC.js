// const stdin = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const stdin = require("fs").readFileSync("test.txt").toString().split("\r\n");
const input = (() => {
  let l = 0;
  return () => stdin[l++];
})();

const T = +input();
for (let tc = 0; tc < T; tc++) {
  const cmd = input().split("");
  const _ = +input();
  const arr = input()
    .replace(/[\[\]]/g, "")
    .split(",")
    .filter((v) => v)
    .map(Number);

  let idx = 0;
  let rCnt = 0;
  let check = false;

  cmd.forEach((c) => {
    if (c === "R") {
      rCnt++;
      idx = idx === 0 ? arr.length - 1 : 0;
    } else {
      if (arr.length === 0) {
        check = true;
        return;
      }
      arr.splice(idx, 1);
      if (idx > 0) idx -= 1;
    }
  });
  console.log(
    check
      ? "error"
      : rCnt % 2
      ? JSON.stringify(arr.reverse())
      : JSON.stringify(arr)
  );
}
