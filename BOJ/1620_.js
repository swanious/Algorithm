const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [n, m] = input[0].split(" ");
n = parseInt(n);
m = parseInt(m);
input.shift();
let PM = input.slice(0, n).map((pro) => pro.split("\r").join(""));
PM.unshift("");

let MP = {};
let count = 0;
for (let pm of PM) {
  MP[pm] = count;
  count += 1;
}

const problem = input.slice(n, n + m).map((pro) => pro.split("\r").join(""));

for (let i = 0; i < problem.length; i++) {
  if (
    "0".charCodeAt() <= problem[i].charCodeAt() &&
    problem[i].charCodeAt() <= "9".charCodeAt()
  ) {
    console.log(PM[parseInt(problem[i])]);
  } else {
    console.log(MP[problem[i]]);
  }
}
