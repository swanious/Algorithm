const fs = require("fs")
const n = fs.readFileSync('/dev/stdin').toString().split('\n')
const len = parseInt(n[0])

let arr = new Array(110)
for (let i =0; i < 110; i++) {
  arr[i] = new Array(110)
}

for (let i=1; i < len + 1; i++) {
  var b = n[i].split(' ')
  b = b.map(a => parseInt(a))

  let x1 = b[0];
  let y1 = b[1];
  let width = b[2];
  let height = b[3];

  for (let j=y1; j < height + y1; j++) {
    for (let k=x1; k < width + x1; k++) {
      arr[j][k] = i
    }
  }
}

let result = new Array(len)
result.fill(0)

for (let i=0; i < len; i++) {
  for (let j=0; j < 110; j++) {
    for (let k=0; k < 110; k++) {
      if (arr[j][k] === i + 1) {
        result[i] += 1
      }
    }
  }
}

for (const res of result) {
  console.log(res)
}