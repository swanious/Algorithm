const getCombination = function (arr, selectNumber) {
  const res = [];
  if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소를 return

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombination(rest, selectNumber - 1); // 나머지에 대해 조합을 구한다.
    const attached = combinations.map((combination) => [fixed, ...combination]); // 돌아온 조합에 맨 앞의 원소를 붙인다.
    res.push(...attached); // 배열 spread sytax로 모두다 push
  });

  return res;
};

const example = [1, 2, 3, 4];
const result = getCombination(example, 3);
console.log(result);
