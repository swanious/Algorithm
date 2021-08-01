function solution(left, right) {
  let answer = 0;
  const arr = range(left, right);
  answer = arr.reduce((acc, cur) => {
      // 약수의 개수 구하기
      let cnt = 0;
      for (let i = 1; i <= cur; i++) {
          if (Number.isInteger(cur / i)) cnt++
      }
      
      // 약수의 개수에 따라 누적합 구하기
      acc = cnt % 2 === 0 ? acc + cur : acc - cur;
      return acc
  }, 0)
  return answer;
}

// 배열 만들기
const range = (st, ed) => {
  return Array(ed - st + 1).fill().map((_, i, arr) => arr[i] = st++)
}