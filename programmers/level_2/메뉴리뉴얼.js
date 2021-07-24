function solution(orders, course) {
  let answer = [];
  let countObj = {};
  
  orders.map(v => {
      const order = [...v].sort();
      for (let i = 2; i <= order.length; i++) {
          // course에 해당 개수가 존재하지 않으면 skip
          if (!course.includes(i)) continue;
          const orderCombi = getCombinations(order, i);
          orderCombi.map(v => {
              const str = v.join('')
              countObj[str] = countObj[str] ? countObj[str] + 1 : 1;
          })
      }
  })

  const newOrderArr = Object.entries(countObj);
  course.map(c => {
      const candidates = newOrderArr.filter(v => v[0].length === c && v[1] > 1);
      const maxVal = Math.max(...candidates.map(v => v[1]));
      if (candidates.length > 0) {
          candidates.map(v => {
              if (v[1] === maxVal) {
                  answer.push(v[0])
              }
          })    
      }
  })
  return answer.sort();
}

const getCombinations= function (arr, selectNumber) {
const results = [];
if (selectNumber === 1) return arr.map(v=>[v]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

arr.forEach((fixed, index, origin) => {
  const rest = [...origin.slice(index+1)] // 해당하는 fixed를 제외한 나머지 배열 
  const combinations = getCombinations(rest, selectNumber - 1); // 나머지에 대해 순열을 구한다.
  const attached = combinations.map((permutation) => [fixed, ...permutation]); // 돌아온 순열에 대해 떼 놓은(fixed) 값 붙이기
  results.push(...attached); // 배열 spread syntax 로 모두다 push
});

return results; // 결과 담긴 results return
};