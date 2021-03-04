const fs = require('fs')
const temp = fs.readFileSync('/dev/stdin').toString().split('\n')
const gwalho = {
  ']' : '[',
  ')' : '('
}

for (const t of temp) {
  if (t === '.') {
    break
  }
  let status = 'yes';
  let stack = [];
  for (const text of t) {
    if (text === '(' || text === ')' || text ==='[' || text === ']') {
      stack.push(text)
    }
  }

  let temp = [];
  for (let i = 0; i < stack.length; i++) {
    if (stack[i] === '(' || stack[i] === '[') {
      temp.push(stack[i])
    } else {
      if (temp && temp[temp.length - 1] === gwalho[stack[i]]) {
          temp.pop()
          continue
      } else {
        status = 'no'
      }
    }
  }
  if (temp.length > 0) {
    status = 'no'
  }
  console.log(status)
}