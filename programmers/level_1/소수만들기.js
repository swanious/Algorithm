// 조합 풀이
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

// 반복문 풀이
function solution(nums, result) {
  let answer = 0;
  
  // 크기가 3개로 고정돼있으므로, 반복문으로만 처리할 수 있음
  for(let i=0; i<nums.length - 2; i++) {
      for(let j= i + 1; j<nums.length - 1; j++) {
          for(let k= j + 1; k<nums.length; k++) {
              const sum = nums[i] + nums[j] + nums[k];
              const sqrt = Math.sqrt(sum);
              let cnt = 0;
              // 합의 제곱근까지 돌면서 나누어 떨어진다? -> 소수가 아님
              for(let m = 2; m <= sqrt; m++) {
                  if (Number.isInteger(sum / m)) cnt++
              }
              if (cnt === 0) answer++
          } 
      }
  }
  
  return answer;
}