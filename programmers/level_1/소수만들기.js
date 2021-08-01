function solution(nums) {
  var answer = 0;
  
  const combi = combination(nums, 3);
  
  combi.forEach(v => {
      const sum = v.reduce((acc, cur) => acc + cur, 0);
      const sqrt = Math.sqrt(sum);
      
      let cnt = 0;
      for (let i=2; i<=sqrt; i++) {
          if (Number.isInteger(sum / i)) {
              cnt++
          }
      }
      if (cnt === 0) answer++;
  })
  
  return answer;
}

const combination = (arr, selectNum) => {
  let results = [];
  if (selectNum === 1) return arr.map(v => [v]);
  
  arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = combination(rest, selectNum - 1);
      const attached = combinations.map(combination => [fixed, ...combination]);
      
      results.push(...attached)
  })
  
  return results;
}