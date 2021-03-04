const fs = require('fs')
const temp = fs.readFileSync('/dev/stdin').toString().split('\n')

let [n, k] = temp[0].split(' ')
let arr = temp[1].split(' ')
arr = arr.map(a => parseInt(a))
k = parseInt(k)

let i = 0
let j = 0
let maxNumber = -99999999
let sumNumber = 0;
while (j < n) {
  if (j - i === k) {
    if (maxNumber < sumNumber) {
      maxNumber = sumNumber
    }
    sumNumber -= arr[i]
    i += 1
  }
  sumNumber += arr[j]
  j += 1
}
if (maxNumber < sumNumber) {
  maxNumber = sumNumber
}
console.log(maxNumber)