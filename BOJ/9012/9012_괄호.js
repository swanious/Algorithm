const fs = require("fs");

const stdin = fs.readFileSync("/dev/stdin").toString().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const check = (str) => {
  let stack = [];
  for (let s of str) {
    if (stack.length == 0 && s == ")") return false;

    if (stack.length > 0 && s == ")") {
      stack.pop();
    } else {
      stack.push(s);
    }
  }
  return stack.length === 0;
};

const n = Number(input().trim());
for (let i = 0; i < n; i++) {
  const str = input().trim();
  check(str) ? console.log("YES") : console.log("NO");
}
