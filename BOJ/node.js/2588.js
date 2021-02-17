const fs = require('fs')
const input = fs.readFileSync('dev/stdin').toString().split('\n')
const a = parseInt(input[0])
const b = input[1]

for (let i = b.length - 1; i > -1; i--) {
  console.log(a * b[i])
}
console.log(a * b)
console.log(b[1])