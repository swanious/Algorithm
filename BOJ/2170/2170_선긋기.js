// 입출력
const stdin = (require('fs').readFileSync('/dev/stdin').toString()).split('\n')
const input = (() => {
  let l = 0;
  return () => stdin[l++]
})()


const N = Number(input())
const lines = [];
let ans = 0, check = false, start = 0, end = 0;

// 로직
for (let i=0; i<N; i++) {
  lines.push(input().split(' ').map(Number))
}

lines.sort((a, b) => a[0] - b[0])

for (let line of lines) {
  if (!check) {
    start = line[0];
    end = line[1];
    check = true;
    continue
  }
  
  if (line[0] <= end) {
    end = Math.max(line[1], end)
  }
  
  else {
    ans += end - start;
    start = line[0];
    end = line[1];
  }
}
ans += end - start
console.log(ans)