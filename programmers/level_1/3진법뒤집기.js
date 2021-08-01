function solution(n) {
  return parseInt(numToThree(n, ''), 3)    
}

const numToThree = (n, str) => {
  return n === 0 ? str : numToThree(Math.floor(n / 3), str + (n % 3).toString())
}